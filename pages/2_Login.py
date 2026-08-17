"""
Login Page - Intelligent Software Defect Tracking System
Matches the HTML reference design exactly.
"""

import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Login - Intelligent Software Defect Tracking System with Resolution Assistance",
    page_icon="🐛",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Single compact centered form card
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700&display=swap');
    @import url('https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css');
    
    /* Hide Streamlit branding */
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Full page background */
    .stApp {
        background-color: #0f172a !important;
        font-family: 'Inter', sans-serif;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    /* Remove default container padding */
    .main .block-container {
        padding: 0 !important;
        max-width: 450px !important;
        margin: auto !important;
    }
    
    /* Remove all element spacing */
    .element-container {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    div[data-testid="stVerticalBlock"] {
        gap: 0 !important;
    }
    
    div[data-testid="stVerticalBlock"] > div {
        gap: 0 !important;
    }
    
    /* Style the form as the auth card itself */
    .stForm {
        background: #111827 !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 2.5rem !important;
        box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4) !important;
        max-width: 450px !important;
        margin: 2rem auto !important;
    }
    
    /* Input field spacing */
    .stTextInput {
        margin-bottom: 1rem !important;
    }
    
    /* Labels */
    .stTextInput label {
        color: #F8FAFC !important;
        font-weight: 500 !important;
        font-size: 0.875rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    .stCheckbox label {
        color: #94A3B8 !important;
        font-size: 0.875rem !important;
    }
    
    /* White input fields */
    .stTextInput input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #d1d5db !important;
        border-radius: 8px !important;
        padding: 0.75rem 1rem !important;
        padding-right: 2.5rem !important;
        font-size: 1rem !important;
        height: 2.75rem !important;
    }
    
    .stTextInput input:focus {
        border-color: #EF4444 !important;
        box-shadow: 0 0 0 0.25rem rgba(239, 68, 68, 0.25) !important;
    }
    
    .stTextInput input::placeholder {
        color: #6B7280 !important;
    }
    
    /* Password visibility toggle button */
    .stTextInput button[kind="icon"] {
        position: absolute !important;
        right: 0.75rem !important;
        top: 50% !important;
        transform: translateY(-50%) !important;
        background: transparent !important;
        border: none !important;
        color: #6B7280 !important;
        padding: 0.25rem !important;
        width: 1.5rem !important;
        height: 1.5rem !important;
        z-index: 10 !important;
    }
    
    .stTextInput button[kind="icon"]:hover {
        color: #374151 !important;
    }
    
    .stTextInput > div {
        position: relative !important;
    }
    
    /* Checkbox */
    .stCheckbox {
        margin-bottom: 1.5rem !important;
    }
    
    /* Submit button */
    .stFormSubmitButton {
        margin-top: 0 !important;
    }
    
    .stFormSubmitButton button {
        background-color: #F87171 !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.625rem 1.5rem !important;
        font-weight: 500 !important;
        width: 100% !important;
        height: 2.625rem !important;
        font-size: 1rem !important;
    }
    
    .stFormSubmitButton button:hover {
        background-color: #991b1b !important;
    }
</style>
""", unsafe_allow_html=True)

# Single form container acting as the auth card
with st.form("login_form", clear_on_submit=False):
    # Header inside form
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <div style="display: inline-flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
            <i class="bi bi-bug-fill" style="font-size: 2rem; color: #F87171;"></i>
            <span style="font-size: 1.5rem; font-weight: 700; font-family: 'Poppins', sans-serif; color: #F87171;">Intelligent Software Defect Tracking System</span>
        </div>
        <h3 style="color: #F8FAFC; font-family: 'Poppins', sans-serif; font-weight: 700; font-size: 1.5rem; margin: 0.5rem 0;">Welcome Back</h3>
        <p style="color: #94A3B8; font-size: 1rem; margin: 0;">Enter your credentials to access your account.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Email field
    email = st.text_input("Email Address", placeholder="name@company.com", key="email")
    
    # Password field with Forgot Password link
    st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
        <label style="color: #F8FAFC; font-weight: 500; font-size: 0.875rem;">Password</label>
        <a href="#" style="color: #EF4444; font-size: 0.875rem; text-decoration: none;">Forgot Password?</a>
    </div>
    """, unsafe_allow_html=True)
    password = st.text_input("Password", type="password", placeholder="••••••••", key="password", label_visibility="collapsed")
    
    # Remember me checkbox
    remember_me = st.checkbox("Remember me", key="remember")
    
    # Login button
    submitted = st.form_submit_button("Login")
    
    # Bottom link inside form
    st.markdown("""
    <div style="text-align: center; margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid rgba(255, 255, 255, 0.08);">
        <p style="color: #94A3B8; margin: 0;">Don't have an account? <a href="/Signup" style="color: #F87171; font-weight: 500; text-decoration: none;">Sign Up</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    if submitted:
        if email and password:
            st.switch_page("pages/4_Dashboard.py")
        else:
            st.error("Please enter both email and password.")
