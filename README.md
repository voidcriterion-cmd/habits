# Momentum --- Habit Studio

**A privacy-conscious, installable habit tracker for building
consistency one day at a time.**

Track daily habits, monitor weekly progress, build streaks, and keep
encrypted backups in your own Google Drive.

[**Open the app**](https://voidcriterion-cmd.github.io/habits/) ·
[Report a bug](https://github.com/voidcriterion-cmd/habits/issues)
:::

------------------------------------------------------------------------

## Overview

Momentum is a lightweight, browser-based habit tracker built with HTML,
CSS, and vanilla JavaScript. It combines a weekly habit log with
progress summaries and streak analytics in a responsive interface
designed for desktop and mobile use.

The app is a static website and Progressive Web App (PWA). Habit data is
stored in the current browser, while an optional Google Drive
integration can store an encrypted backup in the signed-in user's
private Drive application-data folder.

> **Project status:** Experimental / personal project. Google OAuth,
> Drive backup and restore, offline behaviour, and installation should
> be tested in the target browsers before relying on the app for
> important data. This README describes the implementation currently in
> the repository; it is not a claim of a completed security audit or
> Google verification.

## Features

-   **Habit tracking:** Create habits, choose an emoji, assign a
    category, and set a weekly target from 1 to 7 days.
-   **Weekly matrix:** Mark or unmark habit completion for individual
    days and navigate between weeks.
-   **Progress insights:** Review daily completion summaries, weekly
    charts, category adherence, and current/best streaks.
-   **Category filters:** Organize habits by Health & Fitness,
    Mindfulness, Productivity, and Growth & Skill.
-   **English and Persian UI:** Switch between English and Persian,
    including left-to-right and right-to-left layouts.
-   **Local-first storage:** The working habit dataset is saved in the
    browser using `localStorage`.
-   **Portable backups:** Export habits to a JSON file and import a
    previously exported backup.
-   **Google Drive backup:** With Google authorization, save or restore
    a backup in the app-specific `appDataFolder`.
-   **Client-side backup encryption:** Drive backup payloads use
    AES-256-GCM; a key is derived from the user's backup passphrase with
    PBKDF2-SHA-256. The current format uses 600,000 PBKDF2 iterations
    and fresh random salt and IV values for each backup.
-   **Installable PWA:** Includes a web app manifest, a service worker,
    and installation guidance for supported browsers.
-   **Responsive interface:** Designed for phones, tablets, and desktop
    screens.

## Live demo

**[voidcriterion-cmd.github.io/habits](https://voidcriterion-cmd.github.io/habits/)**

The live site is public. Do not enter information you would not want
stored in your browser or in a backup you control.

## Getting started

### Use the hosted app

1.  Open the [Momentum web
    app](https://voidcriterion-cmd.github.io/habits/).
2.  Add or edit habits and record daily completions.
3.  Use **Backup** to export a JSON copy when needed.
4.  To use Google Drive backup, open **Account**, sign in/authorize
    Google, and set a backup passphrase.
5.  Keep that passphrase somewhere safe. It is not recoverable by the
    app if you forget it.

### Run it locally

This is a static front-end project; no Node.js build step or application
server is required.

1.  Clone the repository:

    ``` bash
    git clone https://github.com/voidcriterion-cmd/habits.git
    cd habits
    ```

2.  Serve the directory over `http://localhost` using a local static
    server. For example, if Python is installed:

    ``` bash
    python -m http.server 8000
    ```

3.  Open `http://localhost:8000` in your browser.

Some browser capabilities, including service workers, require HTTPS or
localhost. Google OAuth also needs to be configured for the origin you
use.

## Google OAuth and Drive setup

Google integration is optional. The app requests the following scopes:

-   `openid`, `email`, `profile` --- identify the Google account in the
    browser.
-   `https://www.googleapis.com/auth/drive.appdata` --- access the
    app-specific application-data folder in that user's Drive.

To configure a Google Cloud project:

1.  Open the [Google Cloud Console](https://console.cloud.google.com/).

2.  Select or create a project and enable the **Google Drive API**.

3.  Configure **Google Auth Platform / OAuth consent screen** with the
    app name, support contact, audience, and developer contact details.

4.  During development, set the app to **Testing** and add the Google
    accounts you want to use under **Test users**.

5.  Create an OAuth client with application type **Web application**.

6.  Add the exact origin serving Momentum under **Authorized JavaScript
    origins**. For the current GitHub Pages deployment, the origin is:

    ``` text
    https://voidcriterion-cmd.github.io
    ```

    Do not include `/habits/`, a path, query string, or trailing page
    filename in the origin.

7.  Ensure the client ID in the app matches the OAuth client created in
    that Google Cloud project.

8.  Test sign-in, Drive backup, restore, and revoking access before
    inviting other users.

Google may require additional configuration or verification before an
OAuth app can be used by the general public. Testing-mode access is
limited to the configured test users and may have token/authorization
limitations. Follow the current [Google OAuth production-readiness
guidance](https://developers.google.com/identity/protocols/oauth2/production-readiness/policy-compliance)
before a public launch.

**Important:** An OAuth client ID used in browser JavaScript is not a
client secret. Never add a client secret, service-account key, private
key, or other credential to this repository.

## Data storage and privacy

Momentum currently has no application backend or server-side database.

-   **Working data:** Habit names, categories, targets, and completion
    history are stored in the browser's `localStorage`. They are not
    encrypted by this app while stored locally.
-   **Account selection:** Google identity is used by the client to
    associate a browser-local dataset with an account profile. This is
    not server-side authentication and does not protect local data from
    someone who can access the same browser profile or its developer
    tools.
-   **Drive backup:** When the user initiates or enables backup, the app
    encrypts the backup in the browser before uploading it to the user's
    Drive application-data folder.
-   **Backup passphrase:** The passphrase is used to derive the
    encryption key. The app cannot recover a forgotten passphrase;
    losing it can make the encrypted backup unrecoverable.
-   **JSON export:** Exported JSON files are not encrypted by this
    feature. Store them somewhere appropriate and delete extra copies
    when no longer needed.
-   **Third-party assets:** The page loads Tailwind CSS from its CDN and
    fonts from Google Fonts. Google Identity Services and Google Drive
    APIs are also used for their respective features. Those services may
    receive normal network metadata when contacted.

Client-side encryption helps protect a copied Drive backup, but it does
**not** protect against a compromised website or malicious JavaScript
served to the browser. A compromised script could potentially access
data before encryption or interact with an active Google authorization.
Do not describe this implementation as end-to-end secure or
independently audited.

## Offline and PWA behaviour

The project includes `manifest.webmanifest` and `sw.js`, and attempts to
register the service worker over HTTPS or localhost. Offline
availability is best-effort: external CDN resources may not be available
on a first offline visit, and Google sign-in/Drive operations require a
network connection.

For the best installation experience, open the hosted site in a
supported browser and use its **Install app** or **Add to Home Screen**
option. iOS and Android installation steps differ by browser.

## Repository structure

``` text
habits/
├── index.html             # Application UI, styles, and JavaScript
├── manifest.webmanifest   # PWA metadata
├── sw.js                  # Service-worker caching behaviour
└── README.md              # Project documentation
```

The repository may contain additional assets or configuration files as
the project evolves. Keep any new runtime dependencies and deployment
requirements documented here.

## GitHub Pages deployment

The app is static and can be deployed directly with GitHub Pages.

1.  Push `index.html`, `manifest.webmanifest`, `sw.js`, and other
    required static assets to the `main` branch.
2.  Open the repository's **Settings → Pages**.
3.  Under **Build and deployment**, choose **Deploy from a branch**.
4.  Select `main` and the `/ (root)` folder, then save.
5.  Wait for the Pages deployment to finish and open the URL shown in
    the Pages settings.
6.  Confirm that the OAuth JavaScript origin matches the published
    site's origin.

GitHub Pages serves the site publicly. Treat every file in the published
repository as public, including source code and client-side
configuration. Never commit secrets, private keys, real user exports, or
personal habit data.

See the official [GitHub Pages publishing
documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Testing checklist

Before using the app as your only habit record, test these scenarios:

-   [ ] Create, edit, complete, and delete habits.
-   [ ] Navigate to previous and current weeks; verify completion counts
    and streaks.
-   [ ] Switch between English and Persian and check RTL layout.
-   [ ] Export JSON, then import it into a test browser profile.
-   [ ] Sign in with an allowed Google test user.
-   [ ] Create a Drive backup and confirm the operation reports success.
-   [ ] Restore into a separate test profile and verify the data.
-   [ ] Try an incorrect backup passphrase and confirm the backup is not
    applied.
-   [ ] Test offline behaviour, reconnecting, and service-worker
    updates.
-   [ ] Test on at least one desktop browser and one mobile browser.

## Known limitations

-   There is no server-side account system, central database, or
    cross-device live sync service. Cross-device transfer depends on
    backup and restore.
-   Local browser storage is not encrypted by the app.
-   Google OAuth is configured in Google Cloud and may remain restricted
    to test users until the applicable verification requirements are
    met.
-   Offline operation is best-effort and does not include Google Drive
    operations.
-   The project has not been represented as having passed a formal
    security audit or full cross-browser test suite.

## Contributing

Issues and pull requests are welcome. When reporting a bug, include:

-   Browser and operating system
-   Steps to reproduce the problem
-   Expected and actual behaviour
-   Relevant console error messages, with access tokens and personal
    information removed

For changes involving storage, encryption, OAuth, or backup
compatibility, explain the security and migration implications in the
pull request.

## License

No license is specified in this repository yet. Unless a license is
added, others should not assume they have permission to reuse, modify,
or redistribute the code. Choose and add a license before inviting
external contributions or presenting the project as open source.
