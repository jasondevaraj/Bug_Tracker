/**
 * Bug Lifecycle Dashboard — Data Processor
 * Loads, parses, cleans, and aggregates the CSV dataset.
 * Depends on Papa Parse (loaded from CDN in index.html).
 */

const DataProcessor = (() => {
  'use strict';

  /* ─── Date columns to parse ─── */
  const DATE_FIELDS = [
    'Date_Reported',
    'Date_Assigned',
    'Date_Fixed',
    'Date_Retested',
    'Date_Closed'
  ];

  /* ─── Numeric columns to coerce ─── */
  const NUMERIC_FIELDS = [
    'Resolution_Time_Hours',
    'Similarity_Score'
  ];

  /* ─── Categorical columns to trim ─── */
  const CATEGORICAL_FIELDS = [
    'Sprint', 'Release_Version', 'Module', 'Feature', 'Component',
    'Severity', 'Priority', 'Status', 'Resolution', 'Root_Cause',
    'Assigned_To', 'Team', 'Bug_Type', 'Reporter', 'QA_Engineer',
    'Environment', 'Operating_System', 'Browser', 'Device',
    'Lifecycle_Stage'
  ];

  /**
   * Load and parse the CSV file.
   * @param {string} csvPath - relative or absolute URL to the CSV
   * @returns {Promise<Object[]>} array of cleaned row objects
   */
  async function loadCSV(csvPath) {
    const response = await fetch(csvPath);
    if (!response.ok) throw new Error(`Failed to fetch CSV: ${response.status}`);
    const text = await response.text();

    return new Promise((resolve, reject) => {
      Papa.parse(text, {
        header: true,
        skipEmptyLines: true,
        complete(results) {
          if (results.errors.length > 0) {
            console.warn('CSV parse warnings:', results.errors);
          }
          const cleaned = results.data.map(cleanRow);
          resolve(cleaned);
        },
        error(err) {
          reject(err);
        }
      });
    });
  }

  /**
   * Clean a single row: parse dates, coerce numbers, trim strings.
   */
  function cleanRow(row) {
    const out = { ...row };

    // Parse dates
    for (const field of DATE_FIELDS) {
      if (out[field] && out[field].trim()) {
        out[field] = new Date(out[field].trim());
        if (isNaN(out[field].getTime())) out[field] = null;
      } else {
        out[field] = null;
      }
    }

    // Coerce numbers
    for (const field of NUMERIC_FIELDS) {
      const val = parseFloat(out[field]);
      out[field] = isNaN(val) ? 0 : val;
    }

    // Trim categorical strings
    for (const field of CATEGORICAL_FIELDS) {
      if (typeof out[field] === 'string') {
        out[field] = out[field].trim();
      }
    }

    return out;
  }

  /* ─── Aggregation Helpers ─── */

  /**
   * Count occurrences of each unique value in a given field.
   * @returns {Object} { value: count, ... }
   */
  function countBy(data, field) {
    const counts = {};
    for (const row of data) {
      const key = row[field] || 'Unknown';
      counts[key] = (counts[key] || 0) + 1;
    }
    return counts;
  }

  /**
   * Group rows by a field value.
   * @returns {Object} { value: [rows], ... }
   */
  function groupBy(data, field) {
    const groups = {};
    for (const row of data) {
      const key = row[field] || 'Unknown';
      if (!groups[key]) groups[key] = [];
      groups[key].push(row);
    }
    return groups;
  }

  /**
   * Compute average of a numeric field, optionally grouped by a category.
   * @param {Object[]} data
   * @param {string} numericField
   * @param {string} [groupField] - if provided, returns { group: avg }
   * @returns {number | Object}
   */
  function averageBy(data, numericField, groupField) {
    if (!groupField) {
      const vals = data.map(r => r[numericField]).filter(v => v > 0);
      return vals.length ? vals.reduce((a, b) => a + b, 0) / vals.length : 0;
    }

    const groups = groupBy(data, groupField);
    const result = {};
    for (const [key, rows] of Object.entries(groups)) {
      const vals = rows.map(r => r[numericField]).filter(v => v > 0);
      result[key] = vals.length ? vals.reduce((a, b) => a + b, 0) / vals.length : 0;
    }
    return result;
  }

  /**
   * Aggregate count by a date field at weekly granularity.
   * @returns {{ labels: string[], values: number[] }}
   */
  function timeSeriesBy(data, dateField, granularity = 'week') {
    // Filter rows with valid dates and sort
    const validRows = data
      .filter(r => r[dateField] instanceof Date)
      .sort((a, b) => a[dateField] - b[dateField]);

    if (validRows.length === 0) return { labels: [], values: [] };

    const buckets = {};

    for (const row of validRows) {
      let key;
      const d = row[dateField];
      if (granularity === 'day') {
        key = d.toISOString().split('T')[0];
      } else {
        // Week: bucket by the Monday of each week
        const monday = new Date(d);
        const day = monday.getDay();
        const diff = (day === 0 ? -6 : 1) - day;
        monday.setDate(monday.getDate() + diff);
        key = monday.toISOString().split('T')[0];
      }
      buckets[key] = (buckets[key] || 0) + 1;
    }

    const sortedKeys = Object.keys(buckets).sort();
    return {
      labels: sortedKeys.map(k => {
        const d = new Date(k);
        return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
      }),
      values: sortedKeys.map(k => buckets[k])
    };
  }

  /**
   * Build a stacked dataset: for each category in groupField,
   * count how many rows fall into each value of stackField.
   * @returns {{ labels: string[], datasets: { label, data }[] }}
   */
  function stackedCountBy(data, groupField, stackField) {
    const groups = groupBy(data, groupField);
    const stackValues = [...new Set(data.map(r => r[stackField] || 'Unknown'))];
    const labels = Object.keys(groups).sort();

    const datasets = stackValues.map(sv => ({
      label: sv,
      data: labels.map(lbl => {
        return groups[lbl].filter(r => (r[stackField] || 'Unknown') === sv).length;
      })
    }));

    return { labels, datasets };
  }

  /**
   * Compute KPI summary metrics.
   */
  function computeKPIs(data) {
    const total = data.length;
    const openBugs = data.filter(r => r.Status === 'Open').length;
    const closedBugs = data.filter(r => r.Status === 'Closed').length;
    const criticalBugs = data.filter(r => r.Severity === 'Critical').length;
    const avgResolution = averageBy(data, 'Resolution_Time_Hours');

    return {
      total,
      openBugs,
      closedBugs,
      criticalBugs,
      avgResolution: Math.round(avgResolution * 10) / 10
    };
  }

  /* ─── Filter State ─── */

  /**
   * Global filter state. Each key maps to a dataset field,
   * and its value is the currently selected filter value ('' = no filter).
   */
  const currentFilters = {
    Sprint: '',
    Release_Version: '',
    Module: '',
    Priority: '',
    Severity: '',
    Status: '',
    searchQuery: ''
  };

  /**
   * Apply all active filters to the dataset and return matching rows.
   * @param {Object[]} data - the full cleaned dataset
   * @param {Object} [filters] - optional override; defaults to currentFilters
   * @returns {Object[]} filtered array
   */
  function applyFilters(data, filters) {
    const f = filters || currentFilters;
    return data.filter(row => {
      // Helper for loose match (case-insensitive trim)
      const matches = (filterVal, rowVal) => {
        if (!filterVal) return true;
        if (!rowVal) return false;
        return String(filterVal).trim().toLowerCase() === String(rowVal).trim().toLowerCase();
      };

      // Dropdown filters
      if (!matches(f.Sprint, row.Sprint)) return false;
      if (!matches(f.Release_Version, row.Release_Version)) return false;
      if (!matches(f.Module, row.Module)) return false;
      if (!matches(f.Priority, row.Priority)) return false;
      if (!matches(f.Severity, row.Severity)) return false;
      if (!matches(f.Status, row.Status)) return false;

      // Keyword search — case-insensitive match on Bug_ID or Bug_Title
      if (f.searchQuery) {
        const q = f.searchQuery.trim().toLowerCase();
        const id = (row.Bug_ID || '').toLowerCase();
        const title = (row.Bug_Title || '').toLowerCase();
        if (!id.includes(q) && !title.includes(q)) return false;
      }

      return true;
    });
  }

  /**
   * Get sorted unique values for a given field (for populating dropdowns).
   * @param {Object[]} data
   * @param {string} field
   * @returns {string[]}
   */
  function getUniqueValues(data, field) {
    const vals = new Set();
    for (const row of data) {
      if (row[field] && row[field].trim()) vals.add(row[field]);
    }
    return [...vals].sort();
  }

  /**
   * Reset all filters to their default empty state.
   */
  function resetFilters() {
    for (const key of Object.keys(currentFilters)) {
      currentFilters[key] = '';
    }
  }

  /* ─── Public API ─── */
  return {
    loadCSV,
    countBy,
    groupBy,
    averageBy,
    timeSeriesBy,
    stackedCountBy,
    computeKPIs,
    currentFilters,
    applyFilters,
    getUniqueValues,
    resetFilters
  };
})();
