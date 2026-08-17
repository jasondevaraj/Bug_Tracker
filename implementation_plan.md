# Intelligent Defect Tracking Dashboard Module — Implementation Plan

Build a fully client-side, interactive analytics dashboard inside `Bug-Lifecycle-Dashboard/` that mirrors the dark-mode visual identity of the existing landing page and visualizes the 200-row CSV dataset.

## Proposed Changes

### Theme & Styling

#### [NEW] [dashboard-theme.css](file:///d:/Jason/Bug-Life-Cycle/Bug-Lifecycle-Dashboard/css/dashboard-theme.css)

Unified CSS custom-property file extracted from the landing page's [style.css](file:///d:/Jason/Bug-Life-Cycle/Bug-Lifecycle-Landing/css/style.css):

| Token | Value | Source |
|---|---|---|
| `--primary-color` | `#F87171` | Landing `:root` |
| `--accent-color` | `#EF4444` | Landing `:root` |
| `--success-color` | `#22C55E` | Landing `:root` |
| `--warning-color` | `#F97316` | Landing `:root` |
| `--danger-color` | `#DC2626` | Landing `:root` |
| `--bg-color` | `#020617` | Landing `:root` |
| `--card-bg` | `#0F172A` | Landing `:root` |
| `--surface-color` | `#111827` | Landing `.section-card`, `.card-custom` |
| `--text-main` | `#F8FAFC` | Landing `:root` |
| `--text-muted` | `#94A3B8` | Landing `:root` |
| `--font-heading` | `'Poppins', sans-serif` | Landing `:root` |
| `--font-body` | `'Inter', sans-serif` | Landing `:root` |
| `--border-radius-sm` | `8px` | Buttons |
| `--border-radius-md` | `20px` | Cards |
| `--border-radius-lg` | `28px` / `30px` | Navbar / Section-card |
| `--shadow-card` | `0 24px 80px rgba(0,0,0,0.4)` | `.card-custom` |
| `--shadow-section` | `0 28px 80px rgba(0,0,0,0.45)` | `.section-card` |
| `--border-subtle` | `1px solid rgba(255,255,255,0.08)` | Cards / sections |

This file will also contain all dashboard-specific layout styles: sidebar, grid, cards, chart containers, and responsive breakpoints — following the same glassmorphism aesthetic of the landing page.

---

### Data Pipeline

#### [NEW] [data-processor.js](file:///d:/Jason/Bug-Life-Cycle/Bug-Lifecycle-Dashboard/js/data-processor.js)

Client-side JS module that:
1. Fetches `../Bug_Life_Cycle_Managementreport.csv` via `fetch()`.
2. Parses CSV using [Papa Parse](https://www.papaparse.com/) (loaded from CDN).
3. Cleans & types the data:
   - Parses the 5 date columns (`Date_Reported`, `Date_Assigned`, `Date_Fixed`, `Date_Retested`, `Date_Closed`) into `Date` objects.
   - Coerces `Resolution_Time_Hours` and `Similarity_Score` to `Number`.
   - Trims whitespace on all categorical fields (`Sprint`, `Release_Version`, `Module`, `Feature`, `Component`, `Severity`, `Priority`, `Status`, `Resolution`, `Root_Cause`, `Assigned_To`, `Team`).
4. Exports aggregate helpers: `countBy()`, `groupBy()`, `averageBy()`, `timeSeriesBy()` for chart consumption.

---

### Dashboard Charts (Chart.js via CDN)

#### [NEW] [dashboard-charts.js](file:///d:/Jason/Bug-Life-Cycle/Bug-Lifecycle-Dashboard/js/dashboard-charts.js)

Renders 8 interactive charts using Chart.js (loaded from CDN), with the theme palette:

| # | Chart Type | What it shows |
|---|---|---|
| 1 | **Doughnut** | Bug Status Distribution (Open / In Progress / Assigned / Fixed / Verified / Closed / New) |
| 2 | **Horizontal Bar** | Bugs by Severity (Critical / High / Medium / Low) |
| 3 | **Stacked Bar** | Bugs by Module × Status |
| 4 | **Bar** | Bugs by Priority (P1–P4) |
| 5 | **Bar** | Average Resolution Time by Team |
| 6 | **Line** | Bug Reporting Trend over time (weekly aggregation) |
| 7 | **Pie** | Resolution Type distribution (Fixed / Duplicate / etc.) |
| 8 | **Radar** | Root Cause Analysis |

All charts use the landing-page color palette with semi-transparent fills. Tooltips, legends, and animations follow Chart.js defaults for interactivity.

---

### Dashboard Page

#### [NEW] [index.html](file:///d:/Jason/Bug-Life-Cycle/Bug-Lifecycle-Dashboard/index.html)

Structure:
- **Navbar** — identical visual style to the landing page navbar (dark glassmorphic pill, bug icon, nav links), with:
  - A "← Back to Home" link pointing to `../Bug-Lifecycle-Landing/index.html`
  - "Dashboard" as the active nav item
- **KPI Cards Row** — 5 summary metric cards at the top:
  - Total Bugs
  - Open Bugs
  - Closed Bugs
  - Avg Resolution Time (hours)
  - Critical Bugs count
- **Charts Grid** — responsive CSS grid (2 columns on desktop, 1 on mobile) containing the 8 chart cards
- **Footer** — matching the landing page footer styling

CDN dependencies (no build tools):
- Bootstrap 5.3.0 (CSS + JS)
- Bootstrap Icons 1.11.1
- Google Fonts (Inter + Poppins)
- Chart.js 4.x
- Papa Parse 5.x

---

## File Structure

```
Bug-Lifecycle-Dashboard/
├── index.html
├── css/
│   └── dashboard-theme.css
└── js/
    ├── data-processor.js
    └── dashboard-charts.js
```

## Verification Plan

### Manual Verification
- Open `Bug-Lifecycle-Dashboard/index.html` in a browser via Live Server.
- Confirm all 8 charts render with correct data from the CSV.
- Confirm the KPI cards show accurate totals.
- Confirm the "Back to Home" link navigates to the landing page.
- Confirm responsive layout works on narrow viewports.
- Verify visual consistency: same dark theme, red accents, card styles, fonts, and border radii as the landing page.
