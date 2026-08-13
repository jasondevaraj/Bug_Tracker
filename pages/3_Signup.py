"""
Bug Lifecycle Management System - Signup Page
Recreates the HTML signup page using Streamlit components.
"""

import streamlit as st
from utils.styling import apply_dark_theme

# Page Configuration
st.set_page_config(
    page_title="Sign Up - Bug Lifecycle Management System",
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
            <h3 style="color: #F8FAFC; font-weight: 700; margin-bottom: 0.5rem;">Create Account</h3>
            <p style="color: #94A3B8; margin-bottom: 0;">Set up your profile to start tracking bugs.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Signup Form
with st.form("signup_form"):
    st.markdown('<label style="color: #F8FAFC; font-weight: 500; display: block; margin-bottom: 0.5rem;">Full Name</label>', unsafe_allow_html=True)
    full_name = st.text_input("Full Name", placeholder="John Doe", label_visibility="collapsed", key="full_name")
    
    st.markdown('<label style="color: #F8FAFC; font-weight: 500; display: block; margin-bottom: 0.5rem;">Username</label>', unsafe_allow_html=True)
    username = st.text_input("Username", placeholder="johndoe123", label_visibility="collapsed", key="username")
    
    st.markdown('<label style="color: #F8FAFC; font-weight: 500; display: block; margin-bottom: 0.5rem;">Email Address</label>', unsafe_allow_html=True)
    email = st.text_input("Email Address", placeholder="name@company.com", label_visibility="collapsed", key="email")
    
    st.markdown('<label style="color: #F8FAFC; font-weight: 500; display: block; margin-bottom: 0.5rem;">Password</label>', unsafe_allow_html=True)
    password = st.text_input("Password", type="password", placeholder="Create a strong password", label_visibility="collapsed", key="password")
    
    st.markdown('<label style="color: #F8FAFC; font-weight: 500; display: block; margin-bottom: 0.5rem;">Confirm Password</label>', unsafe_allow_html=True)
    confirm_password = st.text_input("Confirm Password", type="password", placeholder="Repeat your password", label_visibility="collapsed", key="confirm_password")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    submitted = st.form_submit_button("Create Account", use_container_width=True)
    
    if submitted:
        if full_name and username and email and password and confirm_password:
            if password == confirm_password:
                # Redirect to login page (placeholder logic)
                st.success("Account created successfully! Redirecting to login...")
                st.switch_page("pages/2_Login.py")
            else:
                st.error("Passwords do not match.")
        else:
            st.error("Please fill in all fields.")

# Login Link
st.markdown("""
<div style="text-align: center; margin-top: 2rem; padding-top: 2rem; border-top: 1px solid rgba(255, 255, 255, 0.08);">
    <p style="color: #94A3B8; margin-bottom: 0;">Already have an account? <a href="/Login" target="_self" style="color: #F87171; font-weight: 500; text-decoration: none;">Login</a></p>
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
