# Momentum — Habit Studio

<!-- TODO: take a real screenshot of the dashboard, save it as docs/dashboard.png and uncomment: -->
<!-- ![Dashboard](docs/dashboard.png) -->

Bilingual (English / فارسی, RTL) habit tracker. Static files only — no backend.

## Known limitations
- **Storage:** habits live in `localStorage` per account on this device. Cross-device sync happens only through the optional encrypted Google Drive backup.
- **Offline:** best-effort only, not guaranteed. It needs HTTPS (or localhost), a first online visit, and the external Tailwind/Google Fonts files to have been cached.
- **External services:** Tailwind CSS and Google Fonts load from CDNs; if blocked, styling/fonts may differ.
- **Accounts:** local profiles; the passphrase is never stored (only a PBKDF2 verifier). It encrypts the Drive backup (AES-GCM). A forgotten passphrase cannot be recovered.

## Google Drive setup
1. Google Cloud Console → create an OAuth **Web** client ID; add your site origin to "Authorized JavaScript origins".
2. Enable the Google Drive API; use only the scope `drive.appdata`.
3. Paste the ID into `GOOGLE_CLIENT_ID` in `index.html`.

Deploy `index.html`, `sw.js`, `manifest.webmanifest`, `icon.svg` together (e.g. GitHub Pages).
