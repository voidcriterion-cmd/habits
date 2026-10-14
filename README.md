# Momentum — Habit Studio

**Build consistency. Track progress. Keep your momentum.**

Momentum is a lightweight, responsive habit-tracking web application designed to help you build consistent routines, monitor daily progress, and understand your weekly performance through an interactive dashboard.

🌐 **Live Demo:** [Open Momentum Habit Studio](https://voidcriterion-cmd.github.io/habits/)

## Overview

Momentum turns everyday routines into measurable progress. Create habits, define weekly targets, track daily completions, and review your consistency through a visual weekly dashboard.

The application runs directly in the browser and stores habit data locally on your device.

## Features

- **Habit Management** — Create habits with custom names, emoji icons, categories, and weekly targets.
- **Daily Tracking** — Mark habits as completed or pending for individual days.
- **Weekly Habit Matrix** — Review habit completion across a seven-day period.
- **Progress Dashboard** — View daily completion rates, weekly progress, and summary statistics.
- **Streak Tracking** — Calculate current and longest consecutive-day streaks.
- **Weekly Analytics** — Explore daily completion rates, category adherence, and streak leaders.
- **Category Filters** — Organize habits into Health & Fitness, Mindfulness, Productivity, and Learning.
- **Week Navigation** — Review previous weeks and return to the current week.
- **Bulk Completion** — Mark all habits as completed for the current day.
- **Data Backup & Restore** — Export habit records to JSON and restore them from a backup file.
- **Responsive Interface** — Adapt the dashboard for mobile phones, tablets, and desktop screens.
- **Install Guidance** — Access instructions for adding the application to a mobile device's home screen.
- **Demo Data** — Explore the dashboard using sample habits and completion history.

## Tech Stack

| Technology | Purpose |
|---|---|
| HTML5 | Application structure |
| CSS3 | Custom styling and responsive presentation |
| JavaScript | Habit management, calculations, persistence, and interactions |
| Tailwind CSS CDN | Utility-first styling |
| Web Storage API | Local persistence through `localStorage` |
| Browser APIs | JSON backup, file import, and install-related functionality |
| GitHub Pages | Static website hosting |

## Getting Started

### Use the Live Application

Visit the live demo:

**https://voidcriterion-cmd.github.io/habits/**

No account or installation is required to use the browser-based application.

### Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/voidcriterion-cmd/habits.git
   ```

2. Open the project directory:

   ```bash
   cd habits
   ```

3. Open `index.html` in a modern web browser.

For a more representative local web environment, serve the directory using a local HTTP server.

## Data Storage & Privacy

Momentum stores habit records in the browser's `localStorage`.

- Habit data remains associated with the browser and origin where it was created.
- No application backend or cloud synchronization service is implemented in the current version.
- Data is not automatically synchronized between devices or browsers.
- Use the built-in JSON export feature to create backups and the import feature to restore them.
- Clearing browser storage or using a different browser profile may make locally stored records unavailable.

**Important:** Export your data regularly if your habit history is important to you.

## Deployment

This project is designed for static hosting and can be published with GitHub Pages.

1. Open the repository's **Settings**.
2. Navigate to **Pages**.
3. Under **Build and deployment**, select **Deploy from a branch**.
4. Select the `main` branch and the `/ (root)` folder.
5. Save the configuration and wait for deployment to finish.

Ensure that `index.html` is located in the repository root.

## Project Structure

```text
habits/
├── index.html
└── README.md
```

The current application is implemented as a single HTML file containing its markup, styling, and JavaScript logic.

## Current Scope

Momentum is a client-side application intended for personal habit tracking. It does not currently provide user accounts, server-side storage, or cross-device synchronization.

Although the application includes PWA-related installation and caching logic, offline availability and installation behavior depend on browser support and the implementation's runtime constraints. These capabilities should be tested on the target devices before being relied upon.

## Contributing

Suggestions, bug reports, and improvements are welcome.

1. Open an issue describing the proposed change or problem.
2. Fork the repository if you plan to contribute code.
3. Create a dedicated branch for your changes.
4. Submit a pull request with a clear description of the changes.

## License

No license has been specified yet. Unless a license is added to this repository, others should not assume they have permission to redistribute or reuse the project's code.

---

**Momentum Habit Studio** — Small actions. Consistent progress.
