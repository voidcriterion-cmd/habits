# Momentum — Habit Studio

A simple habit tracker to help you stay consistent. Track weekly progress, build streaks, and back up your data to Google Drive.

**[Open Momentum](https://voidcriterion-cmd.github.io/habits/)**

## Features

- Create habits, set weekly goals, and track daily progress
- View streaks and weekly statistics
- English and Persian interface with RTL support
- Save data in your browser
- Export and import JSON backups
- Optional encrypted Google Drive backups
- Installable PWA with basic offline support

## Run locally

```bash
git clone https://github.com/voidcriterion-cmd/habits.git
cd habits
python -m http.server 8000
```

Open `http://localhost:8000` in your browser.

## Google Drive backup

Google Drive backup is optional. Configure the Google Drive API and OAuth client in Google Cloud, then add this origin under **Authorized JavaScript origins**:

`https://voidcriterion-cmd.github.io`

If the OAuth app is in Testing mode, add your Google account as a test user.

Backups are encrypted in the browser before upload. Keep your passphrase safe; it cannot be recovered if lost.

## Data and privacy

Habit data is stored in your browser and is **not encrypted locally**. JSON exports are also unencrypted. Google Drive backups use client-side encryption. The app has no backend or live cross-device sync; transferring data between devices requires backup and restore.

Offline support is limited, and Google sign-in and Drive backups require an internet connection.

## Built with

HTML, CSS, JavaScript, browser local storage, Web Crypto API, and Google Drive API.

## License

No license has been added yet. Until one is chosen, others should not assume they have permission to reuse or redistribute this code.
