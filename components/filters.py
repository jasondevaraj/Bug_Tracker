"""
Bug Lifecycle Management System - Filter Components
Provides filter toolbar with dropdowns and search for dashboard.
"""

import streamlit as st
import pandas as pd
from typing import Dict


def render_filter_toolbar(df: pd.DataFrame) -> Dict[str, str]:
    """
    Render filter toolbar with 7 dropdown controls + search.
    Returns dictionary of selected filter values.
    
    Args:
        df: Full DataFrame (for populating filter options)
        
    Returns:
        Dictionary of filter field: selected value pairs
    """
    from utils.data_loader import get_unique_values
    
    # Create container with custom styling
    st.markdown("""
    <div style="
        background: rgba(15, 23, 42, 0.8);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(239, 68, 68, 0.25);
        border-left: 3px solid #EF4444;
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4);
    ">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
            <h6 style="margin: 0; font-weight: 600; color: #F8FAFC;">
                <span style="color: #EF4444; margin-right: 0.5rem;">⚙</span>Filters
            </h6>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Create columns for filters - adjusted for better layout
    col1, col2, col3, col4 = st.columns(4)
    col5, col6, col7, col8, col9 = st.columns([1, 1, 1, 1, 0.8])
    
    filters = {}
    
    with col1:
        sprint_options = ['All Sprints'] + get_unique_values(df, 'Sprint')
        filters['Sprint'] = st.selectbox('Sprint', sprint_options, key='filter_sprint')
        if filters['Sprint'] == 'All Sprints':
            filters['Sprint'] = ''
    
    with col2:
        release_options = ['All Releases'] + get_unique_values(df, 'Release_Version')
        filters['Release_Version'] = st.selectbox('Release', release_options, key='filter_release')
        if filters['Release_Version'] == 'All Releases':
            filters['Release_Version'] = ''
    
    with col3:
        module_options = ['All Modules'] + get_unique_values(df, 'Module')
        filters['Module'] = st.selectbox('Module', module_options, key='filter_module')
        if filters['Module'] == 'All Modules':
            filters['Module'] = ''
    
    with col4:
        priority_options = ['All Priorities'] + get_unique_values(df, 'Priority')
        filters['Priority'] = st.selectbox('Priority', priority_options, key='filter_priority')
        if filters['Priority'] == 'All Priorities':
            filters['Priority'] = ''
    
    with col5:
        severity_options = ['All Severities'] + get_unique_values(df, 'Severity')
        filters['Severity'] = st.selectbox('Severity', severity_options, key='filter_severity')
        if filters['Severity'] == 'All Severities':
            filters['Severity'] = ''
    
    with col6:
        status_options = ['All Statuses'] + get_unique_values(df, 'Status')
        filters['Status'] = st.selectbox('Status', status_options, key='filter_status')
        if filters['Status'] == 'All Statuses':
            filters['Status'] = ''
    
    with col7:
        filters['searchQuery'] = st.text_input('Search', placeholder='Bug ID or title...', key='search_input')
    
    with col8:
        # Add empty label to match other controls' label height
        st.markdown('<label style="height: 1.5rem; margin-bottom: 0.5rem; display: block;">&nbsp;</label>', unsafe_allow_html=True)
        if st.button('🔄 Reset', key='btn_reset'):
            for key in st.session_state.keys():
                if key.startswith('filter_') or key == 'search_input':
                    del st.session_state[key]
            st.rerun()
    
    # Custom styling for filter controls - dark blue theme with maximum override specificity
    st.markdown("""
    <style>
    /* ========================================
       FILTER CONTROLS - DARK BLUE THEME
       Maximum specificity to override all Streamlit defaults
       ======================================== */
    
    /* Nuclear option - remove ALL white backgrounds from selectbox area */
    div[data-testid="stSelectbox"],
    div[data-testid="stSelectbox"] *,
    div[data-testid="stSelectbox"] > div,
    div[data-testid="stSelectbox"] > div > div,
    div[data-testid="stSelectbox"] > div > div > div {
        background-color: #111827 !important;
    }
    
    /* Target the BaseWeb select component at all levels */
    div[data-baseweb="select"],
    div[data-baseweb="select"] *,
    div[data-baseweb="select"] > div,
    div[data-baseweb="select"] > div > div,
    div[data-baseweb="select"] div[class*="container"],
    div[data-baseweb="select"] div[class*="control"],
    div[data-baseweb="select"] div[class*="value"],
    div[data-baseweb="select"] div[class*="Input"],
    div[data-baseweb="select"] div[class*="placeholder"],
    div[data-baseweb="select"] div[class*="single"],
    div[data-baseweb="select"] [role="button"],
    div[data-baseweb="select"] [role="button"] > div {
        background-color: #111827 !important;
        background: #111827 !important;
    }
    
    /* Force dark background and border on main control */
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div:first-child,
    div[data-baseweb="select"] > div:nth-child(1) {
        background-color: #111827 !important;
        background: #111827 !important;
        border: 1px solid #374151 !important;
    }
    
    /* Override any inline styles */
    div[data-testid="stSelectbox"] [style*="background"],
    div[data-baseweb="select"] [style*="background"] {
        background-color: #111827 !important;
        background: #111827 !important;
    }
    
    /* Selectbox text color */
    div[data-testid="stSelectbox"] div[data-baseweb="select"] span,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] div,
    div[data-baseweb="select"] span,
    div[data-baseweb="select"] div[class*="singleValue"],
    div[data-baseweb="select"] div[class*="placeholder"] {
        color: #F8FAFC !important;
    }
    
    /* Hover state */
    div[data-testid="stSelectbox"]:hover div[data-baseweb="select"] > div:first-child,
    div[data-baseweb="select"]:hover > div:first-child {
        border-color: #60A5FA !important;
        background-color: #111827 !important;
    }
    
    /* Focus state */
    div[data-testid="stSelectbox"] div[data-baseweb="select"]:focus-within > div:first-child,
    div[data-baseweb="select"]:focus-within > div:first-child {
        border-color: #3B82F6 !important;
        box-shadow: 0 0 0 1px #3B82F6 !important;
        background-color: #111827 !important;
    }
    
    /* Dropdown arrow */
    div[data-testid="stSelectbox"] svg,
    div[data-baseweb="select"] svg,
    div[data-baseweb="select"] svg path {
        fill: #CBD5E1 !important;
        color: #CBD5E1 !important;
    }
    
    /* Input element */
    div[data-testid="stSelectbox"] input,
    div[data-baseweb="select"] input {
        color: #9CA3AF !important;
        background-color: #111827 !important;
    }
    
    /* Dropdown menu popover - all layers */
    div[data-baseweb="popover"],
    div[data-baseweb="popover"] *,
    div[data-baseweb="popover"] > div,
    div[data-baseweb="popover"] > div > div,
    div[role="presentation"],
    div[role="presentation"] > div {
        background-color: #111827 !important;
        background: #111827 !important;
    }
    
    /* Dropdown menu list container */
    ul[role="listbox"],
    ul[role="listbox"] > div,
    div[data-baseweb="menu"],
    div[data-baseweb="menu"] > ul,
    div[data-baseweb="menu"] > div {
        background-color: #111827 !important;
        background: #111827 !important;
        border: 1px solid #374151 !important;
    }
    
    /* Menu items - all states */
    ul[role="listbox"] li,
    div[data-baseweb="menu"] li,
    li[role="option"],
    div[role="option"] {
        background-color: #111827 !important;
        background: #111827 !important;
        color: #F8FAFC !important;
    }
    
    /* Menu item hover */
    ul[role="listbox"] li:hover,
    div[data-baseweb="menu"] li:hover,
    li[role="option"]:hover,
    div[role="option"]:hover {
        background-color: #1E293B !important;
        background: #1E293B !important;
        color: #F8FAFC !important;
    }
    
    /* Menu item selected */
    ul[role="listbox"] li[aria-selected="true"],
    div[data-baseweb="menu"] li[aria-selected="true"],
    li[role="option"][aria-selected="true"],
    div[role="option"][aria-selected="true"] {
        background-color: #2563EB !important;
        background: #2563EB !important;
        color: #F8FAFC !important;
    }
    
    /* ========================================
       LAYOUT AND ALIGNMENT IMPROVEMENTS
       ======================================== */
    
    /* Make all filter column containers flex containers */
    div[data-testid="column"] {
        display: flex !important;
        flex-direction: column !important;
        justify-content: flex-start !important;
        gap: 0 !important;
    }
    
    /* Ensure all selectbox wrappers have consistent structure */
    div[data-testid="stSelectbox"],
    div[data-testid="stTextInput"] {
        display: flex !important;
        flex-direction: column !important;
        margin-bottom: 0 !important;
    }
    
    /* Align all labels consistently */
    div[data-testid="stSelectbox"] label,
    div[data-testid="stTextInput"] label,
    label[data-testid="stWidgetLabel"] {
        color: #E5E7EB !important;
        font-weight: 500 !important;
        margin-bottom: 0.5rem !important;
        height: 1.5rem !important;
        line-height: 1.5rem !important;
        display: block !important;
    }
    
    /* Ensure all input controls have the same height */
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div:first-child,
    div[data-testid="stTextInput"] input {
        height: 38px !important;
        min-height: 38px !important;
        max-height: 38px !important;
    }
    
    /* Remove default margins from button container column */
    div[data-testid="column"]:has(button[kind="secondary"]) {
        display: flex !important;
        flex-direction: column !important;
        justify-content: flex-start !important;
        align-items: stretch !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Remove margins from button wrapper elements */
    div[data-testid="column"]:has(button[kind="secondary"]) > div,
    div[data-testid="column"]:has(button[kind="secondary"]) > div > div {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Text input (Search box) styling */
    div[data-testid="stTextInput"] > div > div > input {
        background-color: #111827 !important;
        border: 1px solid #374151 !important;
        color: #F8FAFC !important;
        caret-color: #F8FAFC !important;
        height: 38px !important;
        min-height: 38px !important;
        max-height: 38px !important;
        box-sizing: border-box !important;
    }
    
    /* Text input placeholder */
    div[data-testid="stTextInput"] > div > div > input::placeholder {
        color: #9CA3AF !important;
        opacity: 1 !important;
    }
    
    /* Text input hover */
    div[data-testid="stTextInput"] > div > div > input:hover {
        border-color: #60A5FA !important;
    }
    
    /* Text input focus */
    div[data-testid="stTextInput"] > div > div > input:focus {
        border-color: #3B82F6 !important;
        box-shadow: 0 0 0 1px #3B82F6 !important;
        outline: none !important;
    }
    
    /* Ensure typed text visible */
    div[data-testid="stTextInput"] > div > div > input:not(:placeholder-shown) {
        color: #F8FAFC !important;
    }
    
    /* ========================================
       RESET BUTTON STYLING
       ======================================== */
    
    button[kind="secondary"][data-testid="baseButton-secondary"] {
        background-color: #7F1D1D !important;
        border: 1px solid #DC2626 !important;
        color: #F8FAFC !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 500 !important;
        font-size: 0.875rem !important;
        transition: all 0.25s ease !important;
        box-shadow: none !important;
        height: 38px !important;
        min-height: 38px !important;
        max-height: 38px !important;
        line-height: 1.5 !important;
        width: auto !important;
        box-sizing: border-box !important;
        margin: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    button[kind="secondary"][data-testid="baseButton-secondary"]:hover {
        background-color: #991B1B !important;
        border: 1px solid #F87171 !important;
        color: #FFFFFF !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1) !important;
    }
    
    button[kind="secondary"][data-testid="baseButton-secondary"]:active {
        background-color: #B91C1C !important;
        transform: scale(0.98) !important;
    }
    
    button[kind="secondary"][data-testid="baseButton-secondary"] p {
        color: #F8FAFC !important;
        font-weight: 500 !important;
        font-size: 0.875rem !important;
        margin: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 0.25rem !important;
    }
    
    /* Make the reset icon red */
    button[kind="secondary"][data-testid="baseButton-secondary"] p::first-letter {
        color: #EF4444 !important;
    }
    
    button[kind="secondary"][data-testid="baseButton-secondary"] {
        font-family: "Source Sans Pro", sans-serif !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    return filters
