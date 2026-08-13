"""
Bug Lifecycle Management System - Navigation Component
Provides reusable navigation bar for all pages.
"""

import streamlit as st


def render_navbar(active_page: str = None):
    """
    Render the navigation bar component.
    
    Args:
        active_page: Name of the currently active page ('landing', 'login', 'signup', 'dashboard')
    """
    navbar_html = """
    <nav style="position: sticky; top: 1rem; z-index: 1100; padding: 1.1rem 2rem; margin: 0 auto 1rem auto; max-width: 1450px; width: calc(100% - 1.5rem); border-radius: 28px; background: rgba(15, 23, 42, 0.94); border: 1px solid rgba(239, 68, 68, 0.45); box-shadow: 0 30px 60px rgba(0, 0, 0, 0.35);">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap;">
            <a href="/" target="_self" style="text-decoration: none; display: flex; align-items: center; color: #F87171; font-size: 2.35rem; margin-right: 2rem;">
                🐛
            </a>
            <div style="display: flex; align-items: center; gap: 0.65rem; flex: 1; justify-content: center;">
                <a href="/#home" style="padding: 0.75rem 1.1rem; border-radius: 999px; color: white; text-decoration: none; transition: all 0.25s ease; font-size: 1rem;">Home</a>
                <a href="/#lifecycle" style="padding: 0.75rem 1.1rem; border-radius: 999px; color: white; text-decoration: none; transition: all 0.25s ease; font-size: 1rem;">Bug Lifecycle</a>
                <a href="/#features" style="padding: 0.75rem 1.1rem; border-radius: 999px; color: white; text-decoration: none; transition: all 0.25s ease; font-size: 1rem;">Features</a>
                <a href="/#why-us" style="padding: 0.75rem 1.1rem; border-radius: 999px; color: white; text-decoration: none; transition: all 0.25s ease; font-size: 1rem;">Why Choose Us</a>
            </div>
            <div style="display: flex; gap: 0.65rem; margin-left: auto;">
                <a href="/Login" target="_self" style="text-decoration: none;">
                    <button style="background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.14); color: white; padding: 0.75rem 1.3rem; border-radius: 999px; cursor: pointer; transition: all 0.25s ease; font-size: 1rem;">Login</button>
                </a>
                <a href="/Signup" target="_self" style="text-decoration: none;">
                    <button style="background-color: #F87171; color: white; border: none; padding: 0.75rem 1.3rem; border-radius: 999px; cursor: pointer; box-shadow: 0 14px 34px rgba(220, 38, 38, 0.35); transition: all 0.25s ease; font-size: 1rem;">Sign Up</button>
                </a>
            </div>
        </div>
    </nav>
    """
    st.markdown(navbar_html, unsafe_allow_html=True)
