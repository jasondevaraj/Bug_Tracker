"""
Bug Lifecycle Management System - Landing Page
Recreates the HTML landing page using Streamlit components.
"""

import streamlit as st
from components.navbar import render_navbar
from components.footer import render_footer
from utils.styling import apply_dark_theme

# Page Configuration
st.set_page_config(
    page_title="Bug Lifecycle Management System",
    page_icon="🐛",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply dark theme styling
apply_dark_theme()

# Render Navigation Bar
render_navbar(active_page='landing')

# Hero Section
st.markdown("""
<div style="padding: 0.5rem 0 5rem 0; min-height: calc(100vh - 80px); display: flex; align-items: center; max-width: 1550px; margin: 0 auto; width: 96%;">
    <div class="section-card" style="background: #111827; border-radius: 30px; padding: 5rem 4.5rem; box-shadow: 0 28px 80px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.08); width: 100%;">
        <div style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 5rem; align-items: center;">
            <div>
                <span style="display: inline-block; margin-bottom: 1.5rem; color: #EF4444; font-weight: 600; text-transform: uppercase; letter-spacing: 0.12em; font-size: 0.9rem;">Bug Lifecycle</span>
                <h1 style="font-size: clamp(2.8rem, 4.5vw, 4.2rem); font-weight: 800; color: #F8FAFC; margin-bottom: 2rem; line-height: 1.15;">Manage software bugs smarter, faster, and more efficiently.</h1>
                <p style="font-size: 1.45rem; color: #94A3B8; margin-bottom: 3rem; line-height: 1.65; max-width: 650px;">Streamline your development process with our red-alert ready bug lifecycle management system. Log, assign, track, and close issues from one central dashboard.</p>
                <div style="display: flex; gap: 1.5rem; flex-wrap: wrap;">
                    <a href="/Signup" target="_self" style="text-decoration: none;">
                        <button style="background-color: #F87171; color: white; border: none; border-radius: 14px; padding: 18px 48px; font-size: 1.2rem; font-weight: 500; cursor: pointer;">Get Started</button>
                    </a>
                    <a href="/Login" target="_self" style="text-decoration: none;">
                        <button style="background-color: #EF4444; color: white; border: none; border-radius: 14px; padding: 18px 48px; font-size: 1.2rem; font-weight: 500; cursor: pointer;">Login</button>
                    </a>
                </div>
            </div>
            <div style="text-align: center; display: flex; align-items: center; justify-content: center;">
                <div style="padding: 5.5rem 4rem; background: rgba(255, 255, 255, 0.06); border-radius: 28px; box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4); border: 1px solid rgba(239, 68, 68, 0.18); width: 100%; max-width: 550px; min-height: 480px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                    <i class="bi bi-bug" style="font-size: 13rem; color: #EF4444; display: block; line-height: 1;"></i>
                    <h4 style="margin-top: 2rem; color: #94A3B8; font-size: 1.15rem;">Track every issue clearly</h4>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Bug Lifecycle Section
st.markdown("""
<div style="padding: 5rem 0; background-color: #111827;">
    <div class="section-card" style="background: #111827; border-radius: 30px; padding: 3.5rem; box-shadow: 0 28px 80px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.08);">
        <div style="text-align: center; margin-bottom: 3rem;">
            <h2 style="font-size: clamp(2rem, 3vw, 2.8rem); color: #F8FAFC; margin-bottom: 1rem;">The Anatomy of a Bug Lifecycle</h2>
            <p style="color: #94A3B8; font-size: 1.1rem;">Track issues transparently from discovery to resolution.</p>
        </div>
        <div style="max-width: 800px; margin: 0 auto 3rem auto; text-align: center;">
            <h3 style="color: #F8FAFC; margin-bottom: 1rem;">What is Bug Lifecycle Management System?</h3>
            <p style="font-size: 1.15rem; color: #94A3B8; line-height: 1.7;">Our system helps development teams manage software issues efficiently. It tracks bugs from creation until closure, ensuring nothing falls through the cracks. By centralizing issue data, it improves team collaboration, increases productivity, and guarantees faster product delivery.</p>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: flex-start; overflow-x: auto; padding-bottom: 1rem;">
            <div style="flex: 1; text-align: center; min-width: 150px; padding: 0 10px;">
                <div style="width: 50px; height: 50px; background-color: #0F172A; border: 2px solid #EF4444; color: #EF4444; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px auto; font-size: 20px;">➕</div>
                <h5 style="color: #F8FAFC; margin-bottom: 0.5rem;">New</h5>
                <p style="color: #94A3B8; font-size: 0.9rem; margin-bottom: 0;">Bug is reported and logged.</p>
            </div>
            <div style="flex: 1; text-align: center; min-width: 150px; padding: 0 10px;">
                <div style="width: 50px; height: 50px; background-color: #0F172A; border: 2px solid #EF4444; color: #EF4444; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px auto; font-size: 20px;">👤</div>
                <h5 style="color: #F8FAFC; margin-bottom: 0.5rem;">Assigned</h5>
                <p style="color: #94A3B8; font-size: 0.9rem; margin-bottom: 0;">Routed to the right developer.</p>
            </div>
            <div style="flex: 1; text-align: center; min-width: 150px; padding: 0 10px;">
                <div style="width: 50px; height: 50px; background-color: #0F172A; border: 2px solid #EF4444; color: #EF4444; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px auto; font-size: 20px;">⚙️</div>
                <h5 style="color: #F8FAFC; margin-bottom: 0.5rem;">In Progress</h5>
                <p style="color: #94A3B8; font-size: 0.9rem; margin-bottom: 0;">Code is being modified.</p>
            </div>
            <div style="flex: 1; text-align: center; min-width: 150px; padding: 0 10px;">
                <div style="width: 50px; height: 50px; background-color: #0F172A; border: 2px solid #EF4444; color: #EF4444; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px auto; font-size: 20px;">🔧</div>
                <h5 style="color: #F8FAFC; margin-bottom: 0.5rem;">Fixed</h5>
                <p style="color: #94A3B8; font-size: 0.9rem; margin-bottom: 0;">Developer resolves the issue.</p>
            </div>
            <div style="flex: 1; text-align: center; min-width: 150px; padding: 0 10px;">
                <div style="width: 50px; height: 50px; background-color: #0F172A; border: 2px solid #EF4444; color: #EF4444; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px auto; font-size: 20px;">📋</div>
                <h5 style="color: #F8FAFC; margin-bottom: 0.5rem;">Testing</h5>
                <p style="color: #94A3B8; font-size: 0.9rem; margin-bottom: 0;">QA verifies the fix.</p>
            </div>
            <div style="flex: 1; text-align: center; min-width: 150px; padding: 0 10px;">
                <div style="width: 50px; height: 50px; background-color: #0F172A; border: 2px solid #22C55E; color: #22C55E; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px auto; font-size: 20px;">✅</div>
                <h5 style="color: #F8FAFC; margin-bottom: 0.5rem;">Closed</h5>
                <p style="color: #94A3B8; font-size: 0.9rem; margin-bottom: 0;">Issue officially resolved.</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Features Section
st.markdown("""
<div style="padding: 5rem 0; background-color: #0f172a;">
    <div class="section-card" style="background: #111827; border-radius: 30px; padding: 3.5rem; box-shadow: 0 28px 80px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.08);">
        <div style="text-align: center; margin-bottom: 3rem;">
            <h2 style="font-size: clamp(2rem, 3vw, 2.8rem); color: #F8FAFC; margin-bottom: 1rem;">Powerful Features</h2>
            <p style="color: #94A3B8; font-size: 1.1rem;">Everything your team needs to ship high-quality software.</p>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
            <div class="card-custom" style="background: #111827; border-radius: 20px; padding: 1.5rem; box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4);">
                <div style="width: 48px; height: 48px; border-radius: 10px; background-color: rgba(220, 38, 38, 0.15); color: #F87171; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 1rem;">🐛</div>
                <h5 style="color: #F8FAFC; margin-bottom: 1rem;">Bug Reporting</h5>
                <p style="color: #94A3B8; margin-bottom: 0;">Easily log new issues with detailed descriptions, environments, and attachments.</p>
            </div>
            <div class="card-custom" style="background: #111827; border-radius: 20px; padding: 1.5rem; box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4);">
                <div style="width: 48px; height: 48px; border-radius: 10px; background-color: rgba(239, 68, 68, 0.15); color: #EF4444; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 1rem;">👥</div>
                <h5 style="color: #F8FAFC; margin-bottom: 1rem;">Bug Assignment</h5>
                <p style="color: #94A3B8; margin-bottom: 0;">Automatically or manually route bugs to the correct module owners.</p>
            </div>
            <div class="card-custom" style="background: #111827; border-radius: 20px; padding: 1.5rem; box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4);">
                <div style="width: 48px; height: 48px; border-radius: 10px; background-color: rgba(220, 38, 38, 0.15); color: #F87171; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 1rem;">🗺️</div>
                <h5 style="color: #F8FAFC; margin-bottom: 1rem;">Lifecycle Tracking</h5>
                <p style="color: #94A3B8; margin-bottom: 0;">Monitor the exact status of any issue in real-time across the workflow.</p>
            </div>
            <div class="card-custom" style="background: #111827; border-radius: 20px; padding: 1.5rem; box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4);">
                <div style="width: 48px; height: 48px; border-radius: 10px; background-color: rgba(239, 68, 68, 0.15); color: #EF4444; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 1rem;">⬆️</div>
                <h5 style="color: #F8FAFC; margin-bottom: 1rem;">Priority & Severity</h5>
                <p style="color: #94A3B8; margin-bottom: 0;">Categorize bugs to ensure critical issues are tackled first.</p>
            </div>
            <div class="card-custom" style="background: #111827; border-radius: 20px; padding: 1.5rem; box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4);">
                <div style="width: 48px; height: 48px; border-radius: 10px; background-color: rgba(220, 38, 38, 0.15); color: #F87171; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 1rem;">💻</div>
                <h5 style="color: #F8FAFC; margin-bottom: 1rem;">Developer Workspace</h5>
                <p style="color: #94A3B8; margin-bottom: 0;">A focused view for developers to see assigned tasks and update statuses.</p>
            </div>
            <div class="card-custom" style="background: #111827; border-radius: 20px; padding: 1.5rem; box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4);">
                <div style="width: 48px; height: 48px; border-radius: 10px; background-color: rgba(239, 68, 68, 0.15); color: #EF4444; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 1rem;">✅</div>
                <h5 style="color: #F8FAFC; margin-bottom: 1rem;">Testing Module</h5>
                <p style="color: #94A3B8; margin-bottom: 0;">Dedicated workflows for QA to approve fixes or reopen issues.</p>
            </div>
            <div class="card-custom" style="background: #111827; border-radius: 20px; padding: 1.5rem; box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4);">
                <div style="width: 48px; height: 48px; border-radius: 10px; background-color: rgba(220, 38, 38, 0.15); color: #F87171; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 1rem;">💬</div>
                <h5 style="color: #F8FAFC; margin-bottom: 1rem;">Comments & Discussion</h5>
                <p style="color: #94A3B8; margin-bottom: 0;">Contextual threads on every bug for seamless team communication.</p>
            </div>
            <div class="card-custom" style="background: #111827; border-radius: 20px; padding: 1.5rem; box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4);">
                <div style="width: 48px; height: 48px; border-radius: 10px; background-color: rgba(239, 68, 68, 0.15); color: #EF4444; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 1rem;">🔔</div>
                <h5 style="color: #F8FAFC; margin-bottom: 1rem;">Notification System</h5>
                <p style="color: #94A3B8; margin-bottom: 0;">Get alerted when bugs are assigned to you or status changes.</p>
            </div>
            <div class="card-custom" style="background: #111827; border-radius: 20px; padding: 1.5rem; box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4);">
                <div style="width: 48px; height: 48px; border-radius: 10px; background-color: rgba(220, 38, 38, 0.15); color: #F87171; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 1rem;">📊</div>
                <h5 style="color: #F8FAFC; margin-bottom: 1rem;">Dashboard & Reports</h5>
                <p style="color: #94A3B8; margin-bottom: 0;">Visualize project health, bottleneck areas, and team velocity.</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Why Choose Us Section
st.markdown("""
<div style="padding: 5rem 0; background-color: #0f172a;">
    <div class="container">
        <div style="text-align: center; margin-bottom: 3rem;">
            <h2 style="font-size: clamp(2rem, 3vw, 2.8rem); color: #F8FAFC; margin-bottom: 1rem;">Why Choose Us</h2>
            <p style="color: #94A3B8; font-size: 1.1rem;">Designed to eliminate friction in your development pipeline.</p>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; max-width: 1200px; margin: 0 auto;">
            <div class="card-custom" style="background: #111827; border-radius: 20px; padding: 1.5rem; display: flex; align-items: center; gap: 1.5rem; box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4);">
                <div style="width: 48px; height: 48px; border-radius: 10px; background-color: rgba(220, 38, 38, 0.15); color: #F87171; display: flex; align-items: center; justify-content: center; font-size: 24px; flex-shrink: 0;">⚡</div>
                <div>
                    <h5 style="color: #F8FAFC; margin-bottom: 0.25rem;">Faster Bug Resolution</h5>
                    <p style="color: #94A3B8; font-size: 0.9rem; margin-bottom: 0;">Clear assignments and workflows cut resolution times in half.</p>
                </div>
            </div>
            <div class="card-custom" style="background: #111827; border-radius: 20px; padding: 1.5rem; display: flex; align-items: center; gap: 1.5rem; box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4);">
                <div style="width: 48px; height: 48px; border-radius: 10px; background-color: rgba(239, 68, 68, 0.15); color: #EF4444; display: flex; align-items: center; justify-content: center; font-size: 24px; flex-shrink: 0;">📁</div>
                <div>
                    <h5 style="color: #F8FAFC; margin-bottom: 0.25rem;">Organized Workflow</h5>
                    <p style="color: #94A3B8; font-size: 0.9rem; margin-bottom: 0;">Never lose track of a bug report in endless email chains again.</p>
                </div>
            </div>
            <div class="card-custom" style="background: #111827; border-radius: 20px; padding: 1.5rem; display: flex; align-items: center; gap: 1.5rem; box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4);">
                <div style="width: 48px; height: 48px; border-radius: 10px; background-color: rgba(220, 38, 38, 0.15); color: #F87171; display: flex; align-items: center; justify-content: center; font-size: 24px; flex-shrink: 0;">👥</div>
                <div>
                    <h5 style="color: #F8FAFC; margin-bottom: 0.25rem;">Easy Collaboration</h5>
                    <p style="color: #94A3B8; font-size: 0.9rem; margin-bottom: 0;">Bridge the gap between QA, Developers, and Management.</p>
                </div>
            </div>
            <div class="card-custom" style="background: #111827; border-radius: 20px; padding: 1.5rem; display: flex; align-items: center; gap: 1.5rem; box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4);">
                <div style="width: 48px; height: 48px; border-radius: 10px; background-color: rgba(239, 68, 68, 0.15); color: #EF4444; display: flex; align-items: center; justify-content: center; font-size: 24px; flex-shrink: 0;">👁️</div>
                <div>
                    <h5 style="color: #F8FAFC; margin-bottom: 0.25rem;">Transparent Tracking</h5>
                    <p style="color: #94A3B8; font-size: 0.9rem; margin-bottom: 0;">Complete visibility over project health and individual performance.</p>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Statistics Section
st.markdown("""
<div style="padding: 5rem 0; background-color: #111827;">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; text-align: center; max-width: 1200px; margin: 0 auto;">
        <div>
            <h2 style="color: #F87171; font-weight: 700; margin-bottom: 0.5rem;">500+</h2>
            <p style="color: #F8FAFC; font-weight: 500; margin-bottom: 0;">Issues Managed</p>
        </div>
        <div>
            <h2 style="color: #EF4444; font-weight: 700; margin-bottom: 0.5rem;">98%</h2>
            <p style="color: #F8FAFC; font-weight: 500; margin-bottom: 0;">Tracking Accuracy</p>
        </div>
        <div>
            <h2 style="color: #F87171; font-weight: 700; margin-bottom: 0.5rem;">24/7</h2>
            <p style="color: #F8FAFC; font-weight: 500; margin-bottom: 0;">Availability</p>
        </div>
        <div>
            <h2 style="color: #EF4444; font-weight: 700; margin-bottom: 0.5rem;">100%</h2>
            <p style="color: #F8FAFC; font-weight: 500; margin-bottom: 0;">Workflow Transparency</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Call-to-Action Section
st.markdown("""
<div style="padding: 5rem 0; background-color: #F87171; text-align: center;">
    <h2 style="color: white; margin-bottom: 1.5rem;">Ready to Streamline Your Bug Management?</h2>
    <p style="color: rgba(255, 255, 255, 0.8); font-size: 1.25rem; margin-bottom: 2rem;">Join modern teams building better software faster.</p>
    <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
        <a href="/Signup" target="_self" style="text-decoration: none;">
            <button style="background-color: #EF4444; color: white; border: none; border-radius: 8px; padding: 12px 32px; font-size: 1.1rem; font-weight: 500; cursor: pointer;">Sign Up Now</button>
        </a>
        <a href="/Login" target="_self" style="text-decoration: none;">
            <button style="background-color: white; color: #F87171; border: none; border-radius: 8px; padding: 12px 32px; font-size: 1.1rem; font-weight: 700; cursor: pointer;">Login</button>
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# Render Footer
render_footer()
