# Guram Magularia — digital resume (Dash)

A single-page professional website built with Dash, matching the reference design:
navy + gold identity, serif display type, curved hero portrait, practice-area cards,
timeline, contact form, dark/light mode and full responsive behaviour.

## Run it

```bash
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:8050

## Files

| File | What it holds |
|---|---|
| `app.py` | All content + page structure. Edit the `CONTENT` block at the top. |
| `assets/styles.css` | Design tokens, layout, dark mode, responsive rules. |
| `assets/site.js` | Mobile menu, scroll-spy, scroll reveals, back-to-top. |
| `assets/profile.png` | Hero portrait. |

Dash serves everything in `assets/` automatically — no imports needed.

## Things to change first

1. **Portrait** — `assets/profile.png` was cut out of the reference mock-up, so it is
   low resolution. Drop in your original photo under the same name. A portrait around
   1200 x 1500 px works best. If the crop sits wrong, adjust `object-position` in
   `.hero__photo img` (`styles.css`).
2. **CV** — put your PDF in `assets/` and name it `Guram_Magularia_CV.pdf`, or change
   `PROFILE["cv_file"]`. Without it the Download CV button 404s.
3. **Contact details, experience, education, skills, languages, licenses, news** —
   all in the `CONTENT` block in `app.py`.
4. **Contact form** — `submit_request()` only validates right now. Add your delivery
   step (SMTP, a form service, or a database write) where the `TODO` comment is.

## Notes

- Fonts (Cormorant Garamond, Lato, Great Vibes) and Font Awesome icons load from CDNs,
  so the page needs internet access. To go fully offline, download them into `assets/`
  and drop the two entries from `external_stylesheets`.
- The theme choice is stored in `localStorage` and applied before first paint, so there
  is no flash of the wrong theme on reload.
- `prefers-reduced-motion` is respected; keyboard focus rings are visible; the layout
  also has a print stylesheet.

## Deploying

`server = app.server` is already exposed, so any WSGI host works:

```bash
pip install gunicorn
gunicorn app:server
```

Render, Railway, Fly.io and PythonAnywhere all run this as-is.
