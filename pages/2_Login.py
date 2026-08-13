"""
Bug Lifecycle Management System - Login Page
Recreates the HTML login page using Streamlit components.
"""

import streamlit as st
from utils.styling import apply_dark_theme

# Page Configuration
st.set_page_config(
    page_title="Login - Bug Lifecycle Management System",
    page_icon="🐛",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Apply dark theme styling
apply_dark_theme()

# Auth Wrapper
st.markdown("""
<div style="min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 2rem 1rem; background-color: #0f172a;">
    <div class="auth-card" style="width: 100%; max-width: 450px; background: #111827; border-radius: 20px; padding: 2.5rem; box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4);">
        <div style="text-align: center; margin-bottom: 2rem;">
            <a href="/" target="_self" style="text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; margin-bottom: 1.5rem;">
                <span style="font-size: 2.5rem;">🐛</span>
                <span style="font-size: 1.5rem; font-weight: 700; color: #F87171; font-family: 'Poppins', sans-serif;">Bug Lifecycle Management System</span>
            </a>
            <h3 style="color: #F8FAFC; font-weight: 700; margin-bottom: 0.5rem;">Welcome Back</h3>
            <p style="color: #94A3B8; margin-bottom: 0;">Enter your credentials to access your account.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Login Form
with st.form("login_form"):
    st.markdown('<label style="color: #F8FAFC; font-weight: 500; display: block; margin-bottom: 0.5rem;">Email Address</label>', unsafe_allow_html=True)
    email = st.text_input("Email Address", placeholder="name@company.com", label_visibility="collapsed", key="email")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('<label style="color: #F8FAFC; font-weight: 500; display: block; margin-bottom: 0.5rem;">Password</label>', unsafe_allow_html=True)
    with col2:
        st.markdown('<a href="#" style="color: #EF4444; font-size: 0.875rem; text-decoration: none; text-align: right; display: block;">Forgot Password?</a>', unsafe_allow_html=True)
    
    password = st.text_input("Password", type="password", placeholder="••••••••", label_visibility="collapsed", key="password")
    
    remember_me = st.checkbox("Remember me", key="remember")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    submitted = st.form_submit_button("Login", use_container_width=True)
    
    if submitted:
        if email and password:
            # Redirect to dashboard (placeholder logic)
            st.switch_page("pages/4_Dashboard.py")
        else:
            st.error("Please enter both email and password.")

# Sign Up Link
st.markdown("""
<div style="text-align: center; margin-top: 2rem; padding-top: 2rem; border-top: 1px solid rgba(255, 255, 255, 0.08);">
    <p style="color: #94A3B8; margin-bottom: 0;">Don't have an account? <a href="/Signup" target="_self" style="color: #F87171; font-weight: 500; text-decoration: none;">Sign Up</a></p>
</div>
""", unsafe_allow_html=True)

# Custom CSS for form styling
st.markdown("""
<style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Form input styling */
    .stTextInput > div > div > input {
        background-color: #0F172A;
        color: #F8FAFC;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        padding: 0.75rem 1rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #EF4444;
        box-shadow: 0 0 0 0.25rem rgba(239, 68, 68, 0.25);
    }
    
    /* Checkbox styling */
    .stCheckbox {
        color: #94A3B8;
        font-size: 0.875rem;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #F87171;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 500;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #991b1b;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)
