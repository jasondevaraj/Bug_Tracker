"""
Bug Lifecycle Management System - Card Components
Provides reusable card components (KPI cards, feature cards, timeline cards).
"""

import streamlit as st


def render_kpi_card(icon: str, value: str, label: str, color_class: str = 'primary'):
    """
    Render a KPI summary card.
    
    Args:
        icon: Icon emoji or HTML
        value: Main value to display
        label: Label text below value
        color_class: Color theme ('primary', 'warning', 'success', 'info', 'danger')
    """
    color_map = {
        'primary': '#F87171',
        'warning': '#F97316',
        'success': '#22C55E',
        'info': '#38BDF8',
        'danger': '#DC2626'
    }
    
    color = color_map.get(color_class, '#F87171')
    
    st.markdown(f"""
    <div class="kpi-card animate-in" style="
        background: rgba(15, 23, 42, 0.8);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4);
        transition: transform 0.2s ease;
        text-align: center;
    ">
        <div style="
            width: 56px;
            height: 56px;
            margin: 0 auto 1rem;
            background: {color}22;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.75rem;
            color: {color};
        ">{icon}</div>
        <div style="
            font-size: 2rem;
            font-weight: 700;
            color: #F8FAFC;
            margin-bottom: 0.5rem;
            font-family: 'Poppins', sans-serif;
        ">{value}</div>
        <div style="
            font-size: 0.875rem;
            color: #94A3B8;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        ">{label}</div>
    </div>
    """, unsafe_allow_html=True)


def render_feature_card(icon: str, title: str, description: str):
    """
    Render a feature highlight card.
    
    Args:
        icon: Icon emoji or HTML
        title: Feature title
        description: Feature description
    """
    # Placeholder for feature card implementation
    # Will be implemented in Phase 2
    pass


def render_timeline_step(icon: str, title: str, description: str):
    """
    Render a timeline step card.
    
    Args:
        icon: Icon emoji or HTML
        title: Step title
        description: Step description
    """
    # Placeholder for timeline step implementation
    # Will be implemented in Phase 2
    pass
