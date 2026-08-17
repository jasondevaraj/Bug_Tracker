"""Pixel-close Streamlit recreation of the HTML landing-page reference."""

import streamlit as st

st.set_page_config(
    page_title="Intelligent Software Defect Tracking System with Resolution Assistance",
    page_icon="🐛", layout="wide", initial_sidebar_state="collapsed",
)

# HTML-styled controls below use local query actions; Streamlit performs the
# actual current-tab page transition through its native router.
navigation_target = st.query_params.get("navigate")
if navigation_target == "login":
    st.query_params.clear()
    st.switch_page("pages/2_Login.py")
elif navigation_target == "signup":
    st.query_params.clear()
    st.switch_page("pages/3_Signup.py")

features = [
    ("bi-bug", "Bug Reporting", "Easily log new issues with detailed descriptions, environments, and attachments.", "primary"),
    ("bi-person-lines-fill", "Bug Assignment", "Automatically or manually route bugs to the correct module owners.", "accent"),
    ("bi-signpost-split", "Lifecycle Tracking", "Monitor the exact status of any issue in real-time across the workflow.", "primary"),
    ("bi-sort-up", "Priority & Severity", "Categorize bugs to ensure critical issues are tackled first.", "accent"),
    ("bi-code-slash", "Developer Workspace", "A focused view for developers to see assigned tasks and update statuses.", "primary"),
    ("bi-check2-square", "Testing Module", "Dedicated workflows for QA to approve fixes or reopen issues.", "accent"),
    ("bi-chat-dots", "Comments & Discussion", "Contextual threads on every bug for seamless team communication.", "primary"),
    ("bi-bell", "Notification System", "Get alerted when bugs are assigned to you or status changes.", "accent"),
    ("bi-graph-up", "Dashboard & Reports", "Visualize project health, bottleneck areas, and team velocity.", "primary"),
]
steps = [("bi-plus-circle", "New", "Bug is reported and logged."), ("bi-person-check", "Assigned", "Routed to the right developer."), ("bi-gear-wide-connected", "In Progress", "Code is being modified."), ("bi-wrench", "Fixed", "Developer resolves the issue."), ("bi-clipboard-check", "Testing", "QA verifies the fix."), ("bi-check-circle-fill success", "Closed", "Issue officially resolved.")]
benefits = [("bi-lightning-charge", "Faster Bug Resolution", "Clear assignments and workflows cut resolution times in half.", "primary"), ("bi-folder2-open", "Organized Workflow", "Never lose track of a bug report in endless email chains again.", "accent"), ("bi-people", "Easy Collaboration", "Bridge the gap between QA, Developers, and Management.", "primary"), ("bi-eye", "Transparent Tracking", "Complete visibility over project health and individual performance.", "accent")]

feature_cards = "".join(f'<article class="card"><div class="icon {c}"><i class="bi {i}"></i></div><h5>{t}</h5><p>{d}</p></article>' for i, t, d, c in features)
timeline = "".join(f'<div class="step"><div class="round"><i class="bi {i}"></i></div><h5>{t}</h5><p>{d}</p></div>' for i, t, d in steps)
benefit_cards = "".join(f'<article class="benefit"><div class="icon {c}"><i class="bi {i}"></i></div><div><h5>{t}</h5><p>{d}</p></div></article>' for i, t, d, c in benefits)

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700&display=swap');@import url('https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css');
#MainMenu,footer{{visibility:hidden}}[data-testid=stHeader]{{background:transparent}}.stApp,.landing{{background:#0f172a;color:#f8fafc;font-family:Inter,sans-serif}}.main .block-container{{max-width:none;padding:0!important}}.landing *{{box-sizing:border-box}}.landing h1,.landing h2,.landing h3,.landing h4,.landing h5{{font-family:Poppins,sans-serif;color:#f8fafc;margin-top:0}}.landing p{{color:#94a3b8;line-height:1.6;margin-top:0}}.container{{width:min(1200px,calc(100% - 2rem));margin:auto}}.nav{{position:sticky;top:1.5rem;z-index:10;width:min(1200px,calc(100% - 2rem));margin:1.5rem auto 0;padding:.95rem 1rem;border-radius:28px;background:rgba(15,23,42,.94);border:1px solid rgba(239,68,68,.45);box-shadow:0 30px 60px rgba(0,0,0,.35)}}.navin{{display:flex;align-items:center;min-height:38px}}.brand{{font-size:1.75rem;color:#f87171;margin-right:1.5rem}}.links{{display:flex;gap:.5rem;justify-content:center;flex:1}}.links a,.actions a{{color:#fff;text-decoration:none;font-weight:500}}.links a{{padding:.7rem 1rem;border-radius:999px}}.actions{{display:flex;gap:.5rem}}.actions a{{padding:.7rem 1.15rem;border-radius:999px}}.login{{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14)}}.signup{{background:#f87171;box-shadow:0 14px 34px rgba(220,38,38,.35)}}.section{{padding:5rem 0}}.hero{{min-height:calc(100vh - 140px);display:flex;align-items:center}}.surface{{background:#111827;border:1px solid rgba(255,255,255,.08);border-radius:30px;padding:3.5rem;box-shadow:0 28px 80px rgba(0,0,0,.45)}}.hero-grid{{display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:3rem}}.badge{{display:inline-block;margin-bottom:1rem;color:#ef4444;font-weight:600;text-transform:uppercase;letter-spacing:.12em}}.copy h1{{font-size:clamp(2.5rem,4vw,3.5rem);font-weight:700;line-height:1.2;margin-bottom:1.5rem}}.copy p{{font-size:1.25rem;margin-bottom:1.5rem}}.buttons{{display:flex;flex-wrap:wrap;gap:1rem}}.buttons a{{padding:10px 24px;border-radius:8px;color:#fff;text-decoration:none;font-weight:500;font-size:1.25rem}}.primary{{background:#f87171}}.accent{{background:#ef4444}}.bugcard{{min-height:330px;padding:3rem;display:flex;flex-direction:column;align-items:center;justify-content:center;background:rgba(255,255,255,.06);border:1px solid rgba(239,68,68,.18);border-radius:24px;box-shadow:0 24px 80px rgba(0,0,0,.4)}}.bugcard i{{font-size:9rem;color:#ef4444;line-height:1}}.bugcard h4{{color:#94a3b8;margin:1rem 0 0}}.title{{text-align:center;margin-bottom:3rem}}.title h2{{font-size:clamp(2rem,3vw,2.8rem);margin-bottom:.5rem}}.intro{{max-width:800px;margin:0 auto 3rem;text-align:center}}.intro p{{font-size:1.25rem}}.timeline{{display:flex;overflow-x:auto;padding-bottom:1rem}}.step{{flex:1;min-width:150px;padding:0 10px;text-align:center;position:relative}}.step:not(:last-child):after{{content:'';position:absolute;top:24px;left:50%;width:100%;height:2px;background:rgba(255,255,255,.08)}}.round{{position:relative;z-index:1;margin:0 auto 15px;width:50px;height:50px;display:flex;align-items:center;justify-content:center;border:2px solid #ef4444;border-radius:50%;background:#0f172a;color:#ef4444;font-size:20px}}.success{{color:#22c55e}}.step h5{{margin-bottom:.5rem}}.step p{{font-size:.875rem;margin-bottom:0}}.features{{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem}}.card,.benefit{{padding:1.5rem;background:#111827;border-radius:20px;box-shadow:0 24px 80px rgba(0,0,0,.4)}}.card h5{{margin:0 0 1rem}}.card p{{margin:0}}.icon{{width:48px;height:48px;margin-bottom:1rem;display:flex;align-items:center;justify-content:center;border-radius:10px;font-size:24px}}.icon.primary{{background:rgba(220,38,38,.15);color:#f87171}}.icon.accent{{background:rgba(239,68,68,.15);color:#ef4444}}.benefits{{display:grid;grid-template-columns:repeat(2,1fr);gap:1.5rem}}.benefit{{display:flex;align-items:center;gap:1.5rem}}.benefit .icon{{margin:0;flex:0 0 auto}}.benefit h5{{margin:0 0 .25rem}}.benefit p{{margin:0;font-size:.875rem}}.stats{{background:#111827}}.statgrid{{display:grid;grid-template-columns:repeat(4,1fr);gap:1.5rem;padding:5rem 0;text-align:center}}.statgrid h2{{font-weight:700;color:#f87171;margin-bottom:.25rem}}.statgrid div:nth-child(even) h2{{color:#ef4444}}.statgrid p{{color:#f8fafc;font-weight:500;margin:0}}.cta{{padding:5rem 1rem;text-align:center;background:#f87171}}.cta h2,.cta p{{color:#fff}}.cta p{{font-size:1.25rem;color:rgba(255,255,255,.75);margin-bottom:1.5rem}}.cta .buttons{{justify-content:center}}.light{{background:#fff;color:#f87171!important}}.foot{{padding:2rem 0;background:#111827;border-top:1px solid rgba(255,255,255,.08)}}.footgrid{{display:grid;grid-template-columns:repeat(3,1fr);align-items:center}}.footbrand{{color:#f87171;font:700 1.25rem Poppins,sans-serif}}.footlinks,.social{{text-align:center}}.social{{text-align:right}}.foot a{{color:#94a3b8;text-decoration:none;margin:0 .5rem}}.social a{{font-size:1.25rem}}.copyright{{margin-top:1.5rem;padding-top:1.5rem;border-top:1px solid rgba(255,255,255,.08);text-align:center;color:#94a3b8;font-size:.875rem}}@media(max-width:900px){{.navin{{flex-wrap:wrap;gap:1rem;justify-content:center}}.links{{order:3;flex-basis:100%;flex-wrap:wrap}}.hero-grid,.features{{grid-template-columns:repeat(2,1fr)}}.copy{{grid-column:1/-1}}}}@media(max-width:640px){{.nav{{top:.5rem;margin-top:.5rem}}.links{{display:none}}.surface{{padding:2rem 1.25rem}}.section{{padding:3rem 0}}.hero{{min-height:auto}}.hero-grid,.features,.benefits,.statgrid,.footgrid{{grid-template-columns:1fr}}.bugcard{{min-height:250px}}.timeline{{flex-direction:column;align-items:center}}.step:not(:last-child):after{{display:none}}.step{{margin-bottom:2rem}}.footbrand,.social{{text-align:center}}}}
/* Exact overrides from html_reference/Bug-Lifecycle-Landing/css/style.css. */
.nav {{
    z-index: 1100;
    margin: 0 auto;
}}
.landing .brand,
.landing .brand:visited,
.landing .brand i {{
    color: #F87171 !important;
    text-decoration: none;
}}
.bugcard h4 {{
    font-size: 1.5rem;
}}
.foot {{
    background-color: #0f172a;
}}
html {{ scroll-behavior: smooth; }}
.landing section {{ scroll-margin-top: 6rem; }}
</style>
<main class="landing"><nav class="nav"><div class="navin"><a class="brand" href="#home"><i class="bi bi-bug-fill"></i></a><div class="links"><a href="#home">Home</a><a href="#lifecycle">Defect Tracking</a><a href="#features">Features</a><a href="#why-us">Why Choose Us</a></div><div class="actions"><a class="login" href="?navigate=login">Login</a><a class="signup" href="?navigate=signup">Sign Up</a></div></div></nav>
<section id="home" class="section hero"><div class="container surface"><div class="hero-grid"><div class="copy"><span class="badge">Intelligent Defect Tracking</span><h1>Manage software bugs smarter, faster, and more efficiently.</h1><p>Streamline your development process with the Intelligent Software Defect Tracking System with Resolution Assistance. Log, assign, track, and close issues from one central dashboard.</p><div class="buttons"><a class="primary" href="?navigate=login">Get Started</a><a class="accent" href="?navigate=login">Login</a></div></div><div class="bugcard"><i class="bi bi-bug"></i><h4>Track every issue clearly</h4></div></div></div></section>
<section id="lifecycle" class="section" style="background:#111827"><div class="container surface"><div class="title"><h2>The Anatomy of a Bug Lifecycle</h2><p>Track issues transparently from discovery to resolution.</p></div><div class="intro"><h3>What is the Intelligent Software Defect Tracking System with Resolution Assistance?</h3><p>Our system helps development teams manage software issues efficiently. It tracks bugs from creation until closure, ensuring nothing falls through the cracks. By centralizing issue data, it improves team collaboration, increases productivity, and guarantees faster product delivery.</p></div><div class="timeline">{timeline}</div></div></section>
<section id="features" class="section"><div class="container surface"><div class="title"><h2>Powerful Features</h2><p>Everything your team needs to ship high-quality software.</p></div><div class="features">{feature_cards}</div></div></section>
<section id="why-us" class="section"><div class="container"><div class="title"><h2>Why Choose Us</h2><p>Designed to eliminate friction in your development pipeline.</p></div><div class="benefits">{benefit_cards}</div></div></section><section class="stats"><div class="container statgrid"><div><h2>500+</h2><p>Issues Managed</p></div><div><h2>98%</h2><p>Tracking Accuracy</p></div><div><h2>24/7</h2><p>Availability</p></div><div><h2>100%</h2><p>Workflow Transparency</p></div></div></section><section class="cta"><h2>Ready to Streamline Your Bug Management?</h2><p>Join modern teams building better software faster.</p><div class="buttons"><a class="accent" href="?navigate=signup">Sign Up Now</a><a class="light" href="?navigate=login">Login</a></div></section><footer class="foot"><div class="container"><div class="footgrid"><div class="footbrand"><i class="bi bi-bug-fill"></i> Intelligent Defect Tracking</div><div class="footlinks"><a href="/#home">Home</a><a href="/#features">Features</a><a href="mailto:contact@placeholder.com">Contact</a></div><div class="social"><a href="https://github.com/placeholder"><i class="bi bi-github"></i></a><a href="mailto:contact@placeholder.com"><i class="bi bi-envelope"></i></a></div></div><div class="copyright">© 2026 Intelligent Software Defect Tracking System with Resolution Assistance. All rights reserved.</div></div></footer></main>
""", unsafe_allow_html=True)
