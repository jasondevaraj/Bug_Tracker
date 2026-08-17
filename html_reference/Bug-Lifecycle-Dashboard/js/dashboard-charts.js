/**
 * Intelligent Defect Tracking Dashboard — Chart Renderer + Filter Integration
 * Renders 8 interactive Chart.js visualizations using data from DataProcessor.
 * Manages chart instances for live updates when filters change.
 * Depends on Chart.js 4.x (loaded from CDN).
 */

const DashboardCharts = (() => {
  'use strict';

  /* ─── Theme-aware color palette ─── */
  const PALETTE = [
    '#F87171', // primary
    '#EF4444', // accent
    '#F97316', // warning / orange
    '#FBBF24', // amber
    '#22C55E', // success / green
    '#38BDF8', // info / sky
    '#A78BFA', // violet
    '#F472B6', // pink
    '#2DD4BF', // teal
    '#FB923C', // light orange
  ];

  const PALETTE_ALPHA = PALETTE.map(c => c + '99'); // ~60% opacity

  /* ─── Stored chart instances for live updates ─── */
  const charts = {};

  /* ─── Reference to the full (unfiltered) dataset ─── */
  let fullData = [];

  /* ─── Debounce helper for search input ─── */
  let searchTimer = null;

  /* ─── Chart.js global defaults ─── */
  function applyGlobalDefaults() {
    Chart.defaults.color = '#94A3B8';
    Chart.defaults.borderColor = 'rgba(255,255,255,0.06)';
    Chart.defaults.font.family = "'Inter', sans-serif";
    Chart.defaults.font.size = 12;
    Chart.defaults.plugins.legend.labels.usePointStyle = true;
    Chart.defaults.plugins.legend.labels.pointStyle = 'circle';
    Chart.defaults.plugins.legend.labels.padding = 16;
    Chart.defaults.plugins.tooltip.backgroundColor = 'rgba(15,23,42,0.95)';
    Chart.defaults.plugins.tooltip.titleColor = '#F8FAFC';
    Chart.defaults.plugins.tooltip.bodyColor = '#94A3B8';
    Chart.defaults.plugins.tooltip.borderColor = 'rgba(239,68,68,0.3)';
    Chart.defaults.plugins.tooltip.borderWidth = 1;
    Chart.defaults.plugins.tooltip.cornerRadius = 10;
    Chart.defaults.plugins.tooltip.padding = 12;
    Chart.defaults.animation.duration = 800;
    Chart.defaults.animation.easing = 'easeOutQuart';
  }

  /* ═══════════════════════════════════════════════════════
     Filter Integration: populate dropdowns + bind events
     ═══════════════════════════════════════════════════════ */

  /**
   * Populate a <select> element with unique values from the dataset.
   */
  function populateDropdown(selectId, data, field) {
    const el = document.getElementById(selectId);
    if (!el) return;
    const values = DataProcessor.getUniqueValues(data, field);
    // Keep the first "All …" option, remove dynamically-added ones
    const firstOption = el.options[0];
    el.innerHTML = '';
    el.appendChild(firstOption);
    for (const val of values) {
      const opt = document.createElement('option');
      opt.value = val;
      opt.textContent = val;
      el.appendChild(opt);
    }
  }

  /**
   * Populate all dynamically-filled dropdowns.
   */
  function populateFilterDropdowns(data) {
    populateDropdown('filter-sprint', data, 'Sprint');
    populateDropdown('filter-release', data, 'Release_Version');
    populateDropdown('filter-module', data, 'Module');
    populateDropdown('filter-priority', data, 'Priority');
    populateDropdown('filter-severity', data, 'Severity');
    populateDropdown('filter-status', data, 'Status');
  }

  /**
   * Read current values from all filter controls into DataProcessor.currentFilters.
   */
  function readFilterValues() {
    const f = DataProcessor.currentFilters;
    f.Sprint = document.getElementById('filter-sprint')?.value || '';
    f.Release_Version = document.getElementById('filter-release')?.value || '';
    f.Module = document.getElementById('filter-module')?.value || '';
    f.Priority = document.getElementById('filter-priority')?.value || '';
    f.Severity = document.getElementById('filter-severity')?.value || '';
    f.Status = document.getElementById('filter-status')?.value || '';
    f.searchQuery = document.getElementById('search-input')?.value || '';
  }

  /**
   * Reset all filter controls to their default "All" state.
   */
  function resetAllFilters() {
    document.getElementById('filter-sprint').value = '';
    document.getElementById('filter-release').value = '';
    document.getElementById('filter-module').value = '';
    document.getElementById('filter-priority').value = '';
    document.getElementById('filter-severity').value = '';
    document.getElementById('filter-status').value = '';
    document.getElementById('search-input').value = '';
    DataProcessor.resetFilters();
    updateDashboard();
  }

  /**
   * Update the filter count badge.
   */
  function updateFilterCount(filteredCount, totalCount) {
    const el = document.getElementById('filterCount');
    if (!el) return;

    if (filteredCount === totalCount) {
      el.textContent = `Showing all ${totalCount} records`;
      el.classList.remove('active');
    } else {
      el.textContent = `${filteredCount} of ${totalCount} records`;
      el.classList.add('active');
    }
  }

  /**
   * Bind change/input events to all filter controls.
   */
  function bindFilterEvents() {
    // Dropdown selects
    const selects = document.querySelectorAll('.form-select');
    selects.forEach(sel => {
      sel.addEventListener('change', () => {
        readFilterValues();
        updateDashboard();
      });
    });

    // Keyword search (debounced 250ms)
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
      searchInput.addEventListener('input', () => {
        clearTimeout(searchTimer);
        searchTimer = setTimeout(() => {
          readFilterValues();
          updateDashboard();
        }, 250);
      });
    }

    // Reset button
    const resetBtn = document.getElementById('btn-reset');
    if (resetBtn) {
      resetBtn.addEventListener('click', resetAllFilters);
    }
  }

  /* ═══════════════════════════════════════════════════════
     Chart rendering — each returns a Chart instance
     ═══════════════════════════════════════════════════════ */

  /**
   * 1. Bug Status Distribution — Doughnut
   */
  function renderStatusDoughnut(canvasId, data) {
    const counts = DataProcessor.countBy(data, 'Status');
    const labels = Object.keys(counts);
    const values = Object.values(counts);

    return new Chart(document.getElementById(canvasId), {
      type: 'doughnut',
      data: {
        labels,
        datasets: [{
          data: values,
          backgroundColor: PALETTE.slice(0, labels.length),
          borderColor: '#111827',
          borderWidth: 3,
          hoverOffset: 8
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: '65%',
        radius: '85%',
        plugins: {
          legend: { position: 'right' }
        }
      }
    });
  }

  /**
   * 2. Bugs by Severity — Horizontal Bar
   */
  function renderSeverityBar(canvasId, data) {
    const order = ['Critical', 'High', 'Medium', 'Low'];
    const counts = DataProcessor.countBy(data, 'Severity');
    const labels = order.filter(s => counts[s] !== undefined);
    const values = labels.map(l => counts[l]);
    const colors = ['#DC2626', '#F87171', '#F97316', '#FBBF24'];

    return new Chart(document.getElementById(canvasId), {
      type: 'bar',
      data: {
        labels,
        datasets: [{
          label: 'Bug Count',
          data: values,
          backgroundColor: colors.slice(0, labels.length).map(c => c + 'CC'),
          borderColor: colors.slice(0, labels.length),
          borderWidth: 1,
          borderRadius: 6,
          barPercentage: 0.6,
          maxBarThickness: 32
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        indexAxis: 'y',
        scales: {
          x: { grid: { color: 'rgba(255,255,255,0.04)' }, beginAtZero: true },
          y: { grid: { display: false } }
        },
        plugins: { legend: { display: false } }
      }
    });
  }

  /**
   * 3. Bugs by Module × Status — Stacked Bar
   */
  function renderModuleStatusStacked(canvasId, data) {
    const stacked = DataProcessor.stackedCountBy(data, 'Module', 'Status');

    const datasets = stacked.datasets.map((ds, i) => ({
      ...ds,
      backgroundColor: PALETTE[i % PALETTE.length] + 'CC',
      borderColor: PALETTE[i % PALETTE.length],
      borderWidth: 1,
      borderRadius: 4,
      barPercentage: 0.7,
      maxBarThickness: 32
    }));

    return new Chart(document.getElementById(canvasId), {
      type: 'bar',
      data: { labels: stacked.labels, datasets },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            stacked: true,
            grid: { display: false },
            ticks: { maxRotation: 45, minRotation: 30 }
          },
          y: {
            stacked: true,
            grid: { color: 'rgba(255,255,255,0.04)' },
            beginAtZero: true
          }
        },
        plugins: {
          legend: { position: 'top' }
        }
      }
    });
  }

  /**
   * 4. Bugs by Priority — Bar
   */
  function renderPriorityBar(canvasId, data) {
    const order = ['P1', 'P2', 'P3', 'P4'];
    const counts = DataProcessor.countBy(data, 'Priority');
    const labels = order.filter(p => counts[p] !== undefined);
    const values = labels.map(l => counts[l]);
    const colors = ['#EF4444', '#F87171', '#F97316', '#FBBF24'];

    return new Chart(document.getElementById(canvasId), {
      type: 'bar',
      data: {
        labels,
        datasets: [{
          label: 'Bug Count',
          data: values,
          backgroundColor: colors.map(c => c + 'CC'),
          borderColor: colors,
          borderWidth: 1,
          borderRadius: 6,
          barPercentage: 0.55,
          maxBarThickness: 32
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: { grid: { display: false } },
          y: { grid: { color: 'rgba(255,255,255,0.04)' }, beginAtZero: true }
        },
        plugins: { legend: { display: false } }
      }
    });
  }

  /**
   * 5. Average Resolution Time by Team — Bar
   */
  function renderResolutionByTeam(canvasId, data) {
    const avgs = DataProcessor.averageBy(data, 'Resolution_Time_Hours', 'Team');
    const labels = Object.keys(avgs).sort();
    const values = labels.map(l => Math.round(avgs[l] * 10) / 10);

    return new Chart(document.getElementById(canvasId), {
      type: 'bar',
      data: {
        labels,
        datasets: [{
          label: 'Avg Hours',
          data: values,
          backgroundColor: PALETTE.slice(0, labels.length).map(c => c + 'CC'),
          borderColor: PALETTE.slice(0, labels.length),
          borderWidth: 1,
          borderRadius: 6,
          barPercentage: 0.55,
          maxBarThickness: 32
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: { grid: { display: false } },
          y: {
            grid: { color: 'rgba(255,255,255,0.04)' },
            beginAtZero: true,
            title: { display: true, text: 'Hours', color: '#94A3B8' }
          }
        },
        plugins: { legend: { display: false } }
      }
    });
  }

  /**
   * 6. Bug Reporting Trend — Line
   */
  function renderTrendLine(canvasId, data) {
    const ts = DataProcessor.timeSeriesBy(data, 'Date_Reported', 'week');

    return new Chart(document.getElementById(canvasId), {
      type: 'line',
      data: {
        labels: ts.labels,
        datasets: [{
          label: 'Bugs Reported',
          data: ts.values,
          borderColor: '#F87171',
          backgroundColor: 'rgba(248,113,113,0.12)',
          fill: true,
          tension: 0.4,
          pointBackgroundColor: '#F87171',
          pointBorderColor: '#111827',
          pointBorderWidth: 2,
          pointRadius: 4,
          pointHoverRadius: 7
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            grid: { display: false },
            ticks: { maxRotation: 45, minRotation: 30 }
          },
          y: {
            grid: { color: 'rgba(255,255,255,0.04)' },
            beginAtZero: true,
            title: { display: true, text: 'Count', color: '#94A3B8' }
          }
        },
        plugins: { legend: { display: false } }
      }
    });
  }

  /**
   * 7. Resolution Type Distribution — Pie
   */
  function renderResolutionPie(canvasId, data) {
    const counts = DataProcessor.countBy(data, 'Resolution');
    const labels = Object.keys(counts);
    const values = Object.values(counts);

    return new Chart(document.getElementById(canvasId), {
      type: 'pie',
      data: {
        labels,
        datasets: [{
          data: values,
          backgroundColor: PALETTE.slice(0, labels.length),
          borderColor: '#111827',
          borderWidth: 3,
          hoverOffset: 8
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        radius: '85%',
        plugins: {
          legend: { position: 'right' }
        }
      }
    });
  }

  /**
   * 8. Root Cause Analysis — Radar
   */
  function renderRootCauseRadar(canvasId, data) {
    const counts = DataProcessor.countBy(data, 'Root_Cause');
    const labels = Object.keys(counts);
    const values = Object.values(counts);

    return new Chart(document.getElementById(canvasId), {
      type: 'radar',
      data: {
        labels,
        datasets: [{
          label: 'Root Cause Count',
          data: values,
          backgroundColor: 'rgba(248,113,113,0.18)',
          borderColor: '#F87171',
          pointBackgroundColor: '#EF4444',
          pointBorderColor: '#111827',
          pointBorderWidth: 2,
          pointRadius: 5,
          borderWidth: 2
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          r: {
            beginAtZero: true,
            grid: { color: 'rgba(255,255,255,0.06)' },
            angleLines: { color: 'rgba(255,255,255,0.06)' },
            pointLabels: { color: '#94A3B8', font: { size: 11 } },
            ticks: {
              display: false,
              stepSize: 20
            }
          }
        },
        plugins: { legend: { display: false } }
      }
    });
  }

  /* ═══════════════════════════════════════════════════════
     KPI + Chart Update Pipeline
     ═══════════════════════════════════════════════════════ */

  /**
   * Update KPI card values from filtered data.
   */
  function updateKPIs(data) {
    const kpis = DataProcessor.computeKPIs(data);
    document.getElementById('kpi-total').textContent = kpis.total;
    document.getElementById('kpi-open').textContent = kpis.openBugs;
    document.getElementById('kpi-closed').textContent = kpis.closedBugs;
    document.getElementById('kpi-avg-resolution').textContent = kpis.avgResolution + 'h';
    document.getElementById('kpi-critical').textContent = kpis.criticalBugs;
  }

  /**
   * Destroy all existing chart instances so canvases can be reused.
   */
  function destroyAllCharts() {
    for (const key of Object.keys(charts)) {
      if (charts[key]) {
        charts[key].destroy();
        charts[key] = null;
      }
    }
  }

  /**
   * Render (or re-render) all 8 charts with the given data.
   */
  function renderAllCharts(data) {
    destroyAllCharts();
    charts.status = renderStatusDoughnut('chart-status', data);
    charts.severity = renderSeverityBar('chart-severity', data);
    charts.moduleStatus = renderModuleStatusStacked('chart-module-status', data);
    charts.priority = renderPriorityBar('chart-priority', data);
    charts.resolutionTeam = renderResolutionByTeam('chart-resolution-team', data);
    charts.trend = renderTrendLine('chart-trend', data);
    charts.resolutionType = renderResolutionPie('chart-resolution-type', data);
    charts.rootCause = renderRootCauseRadar('chart-root-cause', data);
  }

  /**
   * Master update function — called whenever any filter changes.
   * Filters the full dataset, updates KPIs, and re-renders all charts.
   */
  function updateDashboard() {
    const filtered = DataProcessor.applyFilters(fullData);
    updateFilterCount(filtered.length, fullData.length);
    updateKPIs(filtered);
    renderAllCharts(filtered);
  }

  /* ═══════════════════════════════════════════════════════
     Public API
     ═══════════════════════════════════════════════════════ */

  /**
   * Initialize the full dashboard: apply defaults, populate filters,
   * bind events, and render the initial (unfiltered) view.
   * @param {Object[]} data - cleaned dataset from DataProcessor.loadCSV()
   */
  function init(data) {
    fullData = data;
    applyGlobalDefaults();
    populateFilterDropdowns(data);
    bindFilterEvents();
    updateDashboard();
  }

  /**
   * Legacy entry point — kept for backward compatibility.
   */
  function renderAll(data) {
    init(data);
  }

  return { init, renderAll, updateDashboard };
})();
