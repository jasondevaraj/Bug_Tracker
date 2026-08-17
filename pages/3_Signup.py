"""
Signup Page - Intelligent Software Defect Tracking System
Matches the HTML reference design exactly.
"""

import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Sign Up - Intelligent Software Defect Tracking System with Resolution Assistance",
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
    
    /* Submit button */
    .stFormSubmitButton {
        margin-top: 0.5rem !important;
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
with st.form("signup_form", clear_on_submit=False):
    # Header inside form
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <div style="display: inline-flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
            <i class="bi bi-bug-fill" style="font-size: 2rem; color: #F87171;"></i>
            <span style="font-size: 1.5rem; font-weight: 700; font-family: 'Poppins', sans-serif; color: #F87171;">Intelligent Software Defect Tracking System</span>
        </div>
        <h3 style="color: #F8FAFC; font-family: 'Poppins', sans-serif; font-weight: 700; font-size: 1.5rem; margin: 0.5rem 0;">Create Account</h3>
        <p style="color: #94A3B8; font-size: 1rem; margin: 0;">Set up your profile to start tracking bugs.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Full Name
    full_name = st.text_input("Full Name", placeholder="John Doe", key="full_name")
    
    # Username
    username = st.text_input("Username", placeholder="johndoe123", key="username")
    
    # Email Address
    email = st.text_input("Email Address", placeholder="name@company.com", key="email")
    
    # Password
    password = st.text_input("Password", type="password", placeholder="Create a strong password", key="password")
    
    # Confirm Password
    confirm_password = st.text_input("Confirm Password", type="password", placeholder="Repeat your password", key="confirm_password")
    
    # Create Account button
    submitted = st.form_submit_button("Create Account")
    
    # Bottom link inside form
    st.markdown("""
    <div style="text-align: center; margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid rgba(255, 255, 255, 0.08);">
        <p style="color: #94A3B8; margin: 0;">Already have an account? <a href="/Login" style="color: #F87171; font-weight: 500; text-decoration: none;">Login</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    if submitted:
        if full_name and username and email and password and confirm_password:
            if password == confirm_password:
                st.success("Account created successfully! Redirecting to login...")
                st.switch_page("pages/2_Login.py")
            else:
                st.error("Passwords do not match.")
        else:
            st.error("Please fill in all fields.")
