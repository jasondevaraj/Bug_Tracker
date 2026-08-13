"""
Bug Lifecycle Management System - Styling Utilities
Provides CSS injection system and theme management for Streamlit.
"""

import streamlit as st


def get_theme_vars():
    """
    Returns the design tokens from the HTML reference landing page.
    Maps to CSS variables defined in Bug-Lifecycle-Landing/css/style.css
    """
    return {
        # Colors
        'primary_color': '#F87171',
        'accent_color': '#EF4444',
        'success_color': '#22C55E',
        'warning_color': '#F97316',
        'danger_color': '#DC2626',
        'info_color': '#38BDF8',
        'bg_color': '#020617',
        'card_bg': '#0F172A',
        'surface_color': '#111827',
        'text_main': '#F8FAFC',
        'text_muted': '#94A3B8',
        
        # Typography
        'font_heading': "'Poppins', sans-serif",
        'font_body': "'Inter', sans-serif",
        
        # Border Radii
        'radius_sm': '8px',
        'radius_md': '20px',
        'radius_lg': '28px',
        'radius_xl': '30px',
        'radius_pill': '999px',
        
        # Shadows
        'shadow_card': '0 24px 80px rgba(0, 0, 0, 0.4)',
        'shadow_section': '0 28px 80px rgba(0, 0, 0, 0.45)',
        'shadow_navbar': '0 30px 60px rgba(0, 0, 0, 0.35)',
        'shadow_glow': '0 20px 40px rgba(220, 38, 38, 0.3)',
        
        # Borders
        'border_subtle': '1px solid rgba(255, 255, 255, 0.08)',
        'border_accent': '1px solid rgba(239, 68, 68, 0.45)',
        'border_accent_light': '1px solid rgba(239, 68, 68, 0.18)',
    }


def inject_custom_css():
    """
    Injects custom CSS to match the HTML reference dark theme.
    Applies glassmorphic styling, custom fonts, and component styles.
    """
    theme = get_theme_vars()
    
    css = f"""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700&display=swap');
    
    /* Root Variables */
    :root {{
        --primary-color: {theme['primary_color']};
        --accent-color: {theme['accent_color']};
        --success-color: {theme['success_color']};
        --warning-color: {theme['warning_color']};
        --danger-color: {theme['danger_color']};
        --info-color: {theme['info_color']};
        --bg-color: {theme['bg_color']};
        --card-bg: {theme['card_bg']};
        --surface-color: {theme['surface_color']};
        --text-main: {theme['text_main']};
        --text-muted: {theme['text_muted']};
        --font-heading: {theme['font_heading']};
        --font-body: {theme['font_body']};
    }}
    
    /* Global Styles */
    .stApp {{
        background-color: var(--bg-color);
        font-family: var(--font-body);
    }}
    
    /* Hide Streamlit Branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    /* Headings */
    h1, h2, h3, h4, h5, h6 {{
        font-family: var(--font-heading);
        font-weight: 600;
        color: var(--text-main);
    }}
    
    /* Paragraphs */
    p {{
        color: var(--text-muted);
        line-height: 1.6;
    }}
    
    /* Custom Card Styling */
    .custom-card {{
        background: var(--surface-color);
        border-radius: {theme['radius_md']};
        border: {theme['border_subtle']};
        padding: 1.5rem;
        box-shadow: {theme['shadow_card']};
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    
    .custom-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 32px 90px rgba(0, 0, 0, 0.5);
    }}
    
    /* Button Styling */
    .stButton > button {{
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: {theme['radius_sm']};
        padding: 10px 24px;
        font-weight: 500;
        transition: all 0.3s ease;
    }}
    
    .stButton > button:hover {{
        background-color: #991b1b;
        transform: translateY(-2px);
    }}
    
    /* Input Styling */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select {{
        background-color: var(--card-bg);
        color: var(--text-main);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: {theme['radius_sm']};
    }}
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {{
        background-color: var(--card-bg);
        border-right: {theme['border_subtle']};
    }}
    
    /* Animation for fade-in */
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(16px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    .animate-in {{
        animation: fadeInUp 0.5s ease forwards;
    }}
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)


def apply_dark_theme():
    """
    Applies the complete dark theme styling to the Streamlit app.
    Call this function at the top of each page.
    """
    inject_custom_css()
