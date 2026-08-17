"""
Intelligent Software Defect Tracking System with Resolution Assistance - Dashboard Page
Interactive analytics dashboard with KPI cards, filters, and 8 Chart.js visualizations converted to Plotly.
"""

import streamlit as st
import sys
from pathlib import Path

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.data_loader import load_csv, filter_dataframe
from utils.aggregations import compute_kpis
from utils.styling import apply_dark_theme
from components.cards import render_kpi_card
from components.filters import render_filter_toolbar
from components.charts import (
    render_status_doughnut,
    render_severity_bar,
    render_module_status_stacked,
    render_priority_bar,
    render_resolution_by_team,
    render_trend_line,
    render_resolution_pie,
    render_root_cause_radar
)

# Page config
st.set_page_config(
    page_title="Dashboard — Intelligent Software Defect Tracking System with Resolution Assistance",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply dark theme styling
apply_dark_theme()

# Custom CSS for dashboard-specific styling
st.markdown("""
<style>
/* Dashboard Header */
.dashboard-header {
    text-align: center;
    margin-bottom: 2rem;
    padding: 2rem 0;
}

.dashboard-header h1 {
    font-size: 2.5rem;
    font-weight: 700;
    color: #F8FAFC;
    font-family: 'Poppins', sans-serif;
    margin-bottom: 0.5rem;
}

.dashboard-header p {
    font-size: 1.125rem;
    color: #94A3B8;
    font-weight: 400;
}

/* Chart Card Styling */
.chart-card {
    background: rgba(15, 23, 42, 0.8);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 1.5rem;
    box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4);
    margin-bottom: 1.5rem;
    transition: transform 0.2s ease;
}

.chart-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 32px 90px rgba(0, 0, 0, 0.5);
}

.chart-card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.chart-card-header h3 {
    font-size: 1.25rem;
    font-weight: 600;
    color: #F8FAFC;
    font-family: 'Poppins', sans-serif;
    margin: 0;
}

/* Loading State */
.stSpinner > div {
    border-top-color: #F87171 !important;
}

/* Plotly chart background override */
.js-plotly-plot .plotly .main-svg {
    border-radius: 12px;
}

/* Hide Streamlit elements */
.stDeployButton {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background-color: #020617;
}

/* Filter badge active state */
.badge.active {
    background: rgba(239, 68, 68, 0.25) !important;
    color: #F87171 !important;
    border: 1px solid rgba(239, 68, 68, 0.45);
}

/* Responsive KPI Grid */
@media (max-width: 768px) {
    .dashboard-header h1 {
        font-size: 2rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ═══════════ DASHBOARD CONTENT ═══════════

# Page Header
st.markdown("""
<div class="dashboard-header">
    <h1> Intelligent Software Defect Tracking System with Resolution Assistance</h1>
    <p>Real-time insights from the defect tracking dataset</p>
</div>
""", unsafe_allow_html=True)

# Load data with loading state
try:
    with st.spinner('Loading dashboard data...'):
        df_full = load_csv()
    
    # Render filter toolbar
    filters = render_filter_toolbar(df_full)
    
    # Apply filters to data
    df_filtered = filter_dataframe(df_full, filters)
    
    # Show filter count
    if len(df_filtered) < len(df_full):
        st.info(f"📊 Showing {len(df_filtered)} of {len(df_full)} records")
    
    # Compute KPIs
    kpis = compute_kpis(df_filtered)
    
    # ─── KPI Cards ───
    st.markdown('<div style="margin: 2rem 0 1rem 0;"></div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        render_kpi_card('🐛', str(kpis['total']), 'Total Bugs', 'primary')
    
    with col2:
        render_kpi_card('⚠️', str(kpis['openBugs']), 'Open Bugs', 'warning')
    
    with col3:
        render_kpi_card('✅', str(kpis['closedBugs']), 'Closed Bugs', 'success')
    
    with col4:
        render_kpi_card('⏱️', f"{kpis['avgResolution']}h", 'Avg Resolution Time', 'info')
    
    with col5:
        render_kpi_card('🔥', str(kpis['criticalBugs']), 'Critical Bugs', 'danger')
    
    st.markdown('<div style="margin: 3rem 0;"></div>', unsafe_allow_html=True)
    
    # ─── Charts Grid ───
    
    # Row 1: Status Doughnut + Severity Bar
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_status_doughnut(df_filtered)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_severity_bar(df_filtered)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Row 2: Module × Status Stacked (full width)
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_module_status_stacked(df_filtered)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Row 3: Priority Bar + Resolution by Team
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_priority_bar(df_filtered)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_resolution_by_team(df_filtered)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Row 4: Bug Trend Line (full width)
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_trend_line(df_filtered)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Row 5: Resolution Type Pie + Root Cause Radar
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_resolution_pie(df_filtered)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_root_cause_radar(df_filtered)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer spacing
    st.markdown('<div style="margin: 3rem 0;"></div>', unsafe_allow_html=True)

except FileNotFoundError as e:
    st.error(f"""
    ### ❌ CSV File Not Found
    
    {str(e)}
    
    Please ensure the dataset exists in the `data/` directory.
    """)
except Exception as e:
    st.error(f"""
    ### ❌ Error Loading Dashboard
    
    {str(e)}
    
    Please check the console for more details.
    """)
    st.exception(e)

# ═══════════ FOOTER ═══════════
st.markdown("""
<div style="
    margin-top: 4rem;
    padding: 2rem 0;
    text-align: center;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    color: #64748B;
    font-size: 0.875rem;
">
    <div style="margin-bottom: 0.5rem;">
        <span style="color: #F87171; font-size: 1.25rem;">🐛</span>
        <strong style="color: #F8FAFC; margin-left: 0.5rem;">Intelligent Defect Tracking</strong>
    </div>
    <div style="margin-top: 1rem;">
        <a href="/" style="color: #94A3B8; text-decoration: none; margin: 0 1rem;">Home</a>
        <a href="/Landing" style="color: #94A3B8; text-decoration: none; margin: 0 1rem;">Landing</a>
        <a href="/Login" style="color: #94A3B8; text-decoration: none; margin: 0 1rem;">Login</a>
    </div>
    <div style="margin-top: 1rem; color: #64748B;">
        © 2026 Intelligent Software Defect Tracking System with Resolution Assistance. All rights reserved.
    </div>
</div>
""", unsafe_allow_html=True)
