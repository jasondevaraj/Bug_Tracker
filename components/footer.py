"""
Bug Lifecycle Management System - Footer Component
Provides reusable footer for all pages.
"""

import streamlit as st


def render_footer():
    """
    Render the footer component with brand, links, and copyright.
    """
    footer_html = """
    <footer style="background-color: #0f172a; padding: 2rem 0; border-top: 1px solid rgba(255, 255, 255, 0.08); margin-top: 3rem;">
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 1rem;">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; align-items: center; text-align: center;">
                <div>
                    <h5 style="color: #F87171; font-weight: 700; margin-bottom: 0; display: flex; align-items: center; gap: 0.5rem; justify-content: center; font-family: 'Poppins', sans-serif;">
                        <span style="font-size: 1.5rem;">🐛</span> Bug Lifecycle Management System
                    </h5>
                </div>
                <div style="display: flex; gap: 1.5rem; justify-content: center;">
                    <a href="#" style="color: #94A3B8; text-decoration: none; transition: color 0.2s;">Home</a>
                    <a href="#" style="color: #94A3B8; text-decoration: none; transition: color 0.2s;">Features</a>
                    <a href="#" style="color: #94A3B8; text-decoration: none; transition: color 0.2s;">Contact</a>
                </div>
                <div style="display: flex; gap: 1.5rem; justify-content: center; font-size: 1.25rem;">
                    <a href="https://github.com/placeholder" style="color: #94A3B8; text-decoration: none; transition: color 0.2s;">
                        <span style="font-size: 1.25rem;">📦</span>
                    </a>
                    <a href="mailto:contact@placeholder.com" style="color: #94A3B8; text-decoration: none; transition: color 0.2s;">
                        <span style="font-size: 1.25rem;">✉️</span>
                    </a>
                </div>
            </div>
            <hr style="border: none; border-top: 1px solid rgba(255, 255, 255, 0.08); margin: 2rem 0;">
            <div style="text-align: center; color: #94A3B8; font-size: 0.875rem;">
                © 2026 Bug Lifecycle Management System. All rights reserved.
            </div>
        </div>
    </footer>
    """
    st.markdown(footer_html, unsafe_allow_html=True)
