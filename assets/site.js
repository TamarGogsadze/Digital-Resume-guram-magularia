/* =========================================================
   Guram Magularia — site behaviour
   Dash renders the DOM after this file loads, so everything
   here is either delegated or (re)initialised by a MutationObserver.
   ========================================================= */

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
