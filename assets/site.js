/* =========================================================
   Guram Magularia — site behaviour
   Dash renders the DOM after this file loads, so everything
   here is either delegated or (re)initialised by a MutationObserver.
   ========================================================= */

/* =========================================================
   Dash clientside functions (namespace "gm")
   Referenced from app.py with ClientsideFunction.
   ========================================================= */

window.dash_clientside = window.dash_clientside || {};
window.dash_clientside.gm = Object.assign({}, window.dash_clientside.gm, {

  // Keeps <html lang> and the tab title in step with the chosen language.
  applyLang: function (cfg) {
    if ("speechSynthesis" in window) { window.speechSynthesis.cancel(); }
    if (cfg) {
      document.documentElement.setAttribute("lang", cfg.lang || "en");
      if (cfg.title) { document.title = cfg.title; }
    }
    return window.dash_clientside.no_update;
  },

  // Dark / light mode, remembered between visits.
  toggleTheme: function (n) {
    var root = document.documentElement;
    var current = root.getAttribute("data-theme") || "light";
    if (n) {
      current = current === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", current);
      try { localStorage.setItem("gm-theme", current); } catch (e) {}
    }
    return current === "dark" ? "fa-solid fa-sun" : "fa-solid fa-moon";
  },

  // Reads the welcome aloud, using the voice built into the visitor's
  // browser, in whichever language the page is currently showing.
  speakAbout: function (n, cfg) {
    var idle = "fa-solid fa-volume-high";
    var busy = "fa-solid fa-stop";

    if (!n || !("speechSynthesis" in window)) { return idle; }

    // Second press stops playback.
    if (window.speechSynthesis.speaking || window.speechSynthesis.pending) {
      window.speechSynthesis.cancel();
      return idle;
    }

    var text = (cfg && cfg.speech) ? cfg.speech : "";
    if (!text) { return idle; }

    var lang = (cfg && cfg.lang === "ka") ? "ka-GE" : "en-GB";
    var u = new SpeechSynthesisUtterance(text);
    u.lang = lang;
    u.rate = 0.95;
    u.pitch = 1;

    // Prefer a voice that actually matches the language, when one exists.
    var voices = window.speechSynthesis.getVoices() || [];
    for (var i = 0; i < voices.length; i++) {
      if (voices[i].lang && voices[i].lang.indexOf(lang.slice(0, 2)) === 0) {
        u.voice = voices[i];
        break;
      }
    }

    function reset() {
      var icon = document.getElementById("speak-icon");
      if (icon) { icon.className = idle; }
    }
    u.onend = reset;
    u.onerror = reset;

    window.speechSynthesis.speak(u);
    return busy;
  },

  // Consultation form: opens the visitor's own mail app with the request
  // pre-written. Nothing is sent until they press send there.
  mailtoRequest: function (n, cfg, name, email, message) {
    if (!n || !cfg) { return window.dash_clientside.no_update; }

    name = (name || "").trim();
    email = (email || "").trim();
    message = (message || "").trim();

    var missing = [];
    if (!name) { missing.push(cfg.f_name); }
    if (!email) { missing.push(cfg.f_email); }
    if (!message) { missing.push(cfg.f_message); }
    if (missing.length) {
      return [cfg.m_fill + missing.join(", ") + ".", "form-status err"];
    }
    if (email.indexOf("@") < 0 || email.split("@").pop().indexOf(".") < 0) {
      return [cfg.m_bad_email, "form-status err"];
    }

    var body =
      cfg.label_name + ": " + name + "\n\n" +
      cfg.label_message + ": " + message;

    window.location.href =
      "mailto:" + cfg.email +
      "?subject=" + encodeURIComponent(cfg.subject) +
      "&body=" + encodeURIComponent(body);

    return [cfg.m_opening, "form-status ok"];
  }

});


(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Scroll reveals only apply when this script is alive — without it the
  // page still renders every section at full opacity.
  document.documentElement.classList.add("has-js");

  /* ---------- Mobile menu (delegated) ---------- */
  document.addEventListener("click", function (e) {
    var toggle = e.target.closest("#nav-toggle");
    var nav = document.getElementById("primary-nav");
    if (!nav) return;

    if (toggle) {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      var icon = toggle.querySelector("i");
      if (icon) icon.className = open ? "fa-solid fa-xmark" : "fa-solid fa-bars";
      return;
    }
    // close the menu after tapping a link
    if (e.target.closest("#primary-nav a")) {
      nav.classList.remove("is-open");
      var t = document.getElementById("nav-toggle");
      if (t) {
        t.setAttribute("aria-expanded", "false");
        var i2 = t.querySelector("i");
        if (i2) i2.className = "fa-solid fa-bars";
      }
    }
  });

  /* ---------- Back to top ---------- */
  document.addEventListener("click", function (e) {
    if (e.target.closest("#to-top")) {
      window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" });
    }
  });

  /* ---------- Header shadow + back-to-top visibility ---------- */
  function onScroll() {
    var header = document.querySelector(".header");
    var top = document.getElementById("to-top");
    var y = window.scrollY || document.documentElement.scrollTop;
    if (header) header.classList.toggle("is-stuck", y > 12);
    if (top) top.classList.toggle("is-visible", y > 600);
  }
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---------- Scroll-spy for the nav ---------- */
  var spy = null;
  var visible = new Set();

  function paintActive() {
    var order = Array.prototype.map.call(
      document.querySelectorAll("section[id]"), function (s) { return s.id; }
    );
    var current = order.filter(function (id) { return visible.has(id); })[0];
    document.querySelectorAll("#primary-nav a").forEach(function (a) {
      a.classList.toggle(
        "is-active", !!current && a.getAttribute("href") === "#" + current
      );
    });
  }

  function initSpy() {
    var sections = document.querySelectorAll("section[id]");
    if (!sections.length) return;
    if (spy) { spy.disconnect(); visible.clear(); }

    spy = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) visible.add(entry.target.id);
          else visible.delete(entry.target.id);
        });
        paintActive();
      },
      { rootMargin: "-45% 0px -50% 0px", threshold: 0 }
    );
    sections.forEach(function (s) { spy.observe(s); });
  }

  /* ---------- Reveal on scroll ---------- */
  var revealObserver = new IntersectionObserver(
    function (entries, obs) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          obs.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -60px 0px" }
  );

  function initReveals() {
    document.querySelectorAll(".reveal:not(.is-in)").forEach(function (el, i) {
      if (el.dataset.revealBound) return;
      el.dataset.revealBound = "1";
      el.style.transitionDelay = Math.min(i % 6, 5) * 60 + "ms";
      revealObserver.observe(el);
    });
  }

  function initAll() {
    initSpy();
    initReveals();
    onScroll();
  }

  // Dash mounts the layout asynchronously — watch for it.
  var mo = new MutationObserver(function () {
    clearTimeout(mo._t);
    mo._t = setTimeout(initAll, 60);
  });

  document.addEventListener("DOMContentLoaded", function () {
    initAll();
    var root = document.getElementById("react-entry-point") || document.body;
    mo.observe(root, { childList: true, subtree: true });
  });
})();
