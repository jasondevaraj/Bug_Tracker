"""
Bug Lifecycle Management System - Main Application Entry Point
Configures the application and provides navigation to pages.
"""

import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="Bug Lifecycle Management System",
    page_icon="🐛",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom styling
from utils.styling import apply_dark_theme
apply_dark_theme()

# Main content
st.markdown("""
    <div style="text-align: center; padding: 3rem 1rem;">
        <h1 style="font-size: 3rem; margin-bottom: 1rem;">🐛</h1>
        <h1>Bug Lifecycle Management System</h1>
        <p style="font-size: 1.2rem; color: #94A3B8; margin-top: 1rem;">
            Welcome to the Bug Lifecycle Management System
        </p>
        <p style="color: #94A3B8; margin-top: 2rem;">
            Use the sidebar to navigate to different pages:
        </p>
        <ul style="list-style: none; padding: 0; margin-top: 1.5rem;">
            <li style="margin: 0.5rem 0;"> <strong>Landing</strong> - Home page with features and information</li>
            <li style="margin: 0.5rem 0;"> <strong>Login</strong> - Access your account</li>
            <li style="margin: 0.5rem 0;"> <strong>Signup</strong> - Create a new account</li>
            <li style="margin: 0.5rem 0;"> <strong>Dashboard</strong> - Interactive analytics and reports</li>
        </ul>
    </div>
""", unsafe_allow_html=True)