# Design Document: Streamlit Navigation Improvement

## Overview

This design addresses navigation issues in the Intelligent Software Defect Tracking System with Resolution Assistance Streamlit multipage application. Currently, the application suffers from two critical problems:

1. **Default sidebar visibility**: Streamlit's auto-generated sidebar navigation is visible and interferes with the custom navbar design
2. **Non-functional href navigation**: The custom navbar uses HTML `href` links (e.g., `/Login`, `/Signup`) which don't properly navigate within Streamlit's multipage architecture

The solution will:
- Hide the default Streamlit sidebar completely across all pages using CSS injection
- Replace href-based navigation with Streamlit's `st.switch_page()` API for proper page transitions
- Make Landing page (pages/1_Landing.py) the default entry point by redirecting from app.py
- Preserve all existing files, designs, layouts, and visual styling

This is a **navigation mechanism enhancement only** — no page content, styling, or layouts will be modified.

## Architecture

### Current Architecture

```
Bug-Life-Cycle/
├── app.py                          # Entry point (shows welcome page)
├── .streamlit/config.toml          # Theme configuration
├── pages/
│   ├── 1_Landing.py               # Home page with features
│   ├── 2_Login.py                 # Authentication page
│   ├── 3_Signup.py                # Registration page
│   └── 4_Dashboard.py             # Analytics dashboard
└── components/
    └── navbar.py                  # Custom navigation bar (href-based)
```

**Current Navigation Flow:**
1. User opens app → sees app.py welcome message
2. User clicks navbar link (e.g., "Login") → href="/Login" attempts URL navigation
3. Streamlit's router may or may not handle the href correctly → inconsistent behavior
4. Default sidebar shows all pages → clutters UI and conflicts with custom navbar

### Proposed Architecture

```
Bug-Life-Cycle/
├── app.py                          # Entry point → redirects to Landing
├── .streamlit/config.toml          # Theme configuration (sidebar hidden)
├── pages/
│   ├── 1_Landing.py               # Home page (default view)
│   ├── 2_Login.py                 # Authentication page
│   ├── 3_Signup.py                # Registration page
│   └── 4_Dashboard.py             # Analytics dashboard
└── components/
    └── navbar.py                  # Custom navbar (st.switch_page-based)
```

**Proposed Navigation Flow:**
1. User opens app → app.py immediately redirects to pages/1_Landing.py
2. User clicks navbar button → callback triggers st.switch_page("pages/X_Page.py")
3. Streamlit's router handles page transition properly → consistent behavior
4. Default sidebar is hidden via CSS → clean UI with only custom navbar visible

### Key Architectural Decisions

1. **Preserve Multipage Structure**: Keep all pages in `pages/` folder to maintain Streamlit's multipage architecture rather than consolidating into single-page app
2. **Use st.switch_page() API**: Leverage Streamlit's official navigation API (introduced in v1.28.0) rather than experimental or URL-based approaches
3. **CSS-Based Sidebar Hiding**: Inject CSS to hide sidebar rather than rely on `initial_sidebar_state="collapsed"` which only collapses but doesn't fully hide
4. **Callback-Based Navigation**: Replace href links with Streamlit button callbacks to trigger page switches
5. **Entry Point Redirection**: Make app.py a thin redirect layer to Landing page rather than showing welcome content

## Components and Interfaces

### 1. Modified Entry Point (app.py)

**Purpose**: Redirect immediately to Landing page instead of showing welcome content

**Current Behavior**:
- Displays welcome message with page list
- Relies on user to manually click sidebar

**New Behavior**:
- Calls `st.switch_page("pages/1_Landing.py")` immediately
- No content rendered in app.py (acts as redirect only)

**Interface**:
```python
def main():
    """Entry point that redirects to Landing page"""
    st.switch_page("pages/1_Landing.py")
```

### 2. Modified Navigation Component (components/navbar.py)

**Purpose**: Provide navigation via st.switch_page() instead of href links

**Current Implementation Issues**:
- Uses `<a href="/Login">` which doesn't work reliably in Streamlit
- No callback mechanism for navigation actions
- Hardcoded href values that don't align with Streamlit's page paths

**New Implementation Strategy**:

Since Streamlit's `st.markdown()` with `unsafe_allow_html=True` cannot execute Python callbacks directly, we need a hybrid approach:

1. **Use Streamlit columns layout** for navbar structure
2. **Use st.button()** for navigation elements to trigger st.switch_page()
3. **Apply custom CSS** to style buttons to match original navbar design
4. **Inject CSS** to hide default sidebar

**Interface**:
```python
def render_navbar(active_page: str = None):
    """
    Render navigation bar with st.switch_page() navigation
    
    Args:
        active_page: Currently active page ('landing', 'login', 'signup', 'dashboard')
    """
    # Inject CSS to hide default sidebar and style navbar
    inject_navbar_styles()
    
    # Create navbar layout using Streamlit columns
    cols = st.columns([1, 8, 2])
    
    with cols[0]:
        # Bug icon (home link)
        if st.button("🐛", key="nav_home"):
            st.switch_page("pages/1_Landing.py")
    
    with cols[1]:
        # Navigation links
        nav_cols = st.columns(4)
        with nav_cols[0]:
            if st.button("Home", key="nav_home_text"):
                st.switch_page("pages/1_Landing.py")
        # ... more nav buttons
    
    with cols[2]:
        # Auth buttons
        action_cols = st.columns(2)
        with action_cols[0]:
            if st.button("Login", key="nav_login"):
                st.switch_page("pages/2_Login.py")
        # ... signup button
```

**Alternative Approach (Simpler)**:

Use HTML for navbar structure but add hidden Streamlit buttons that are triggered via CSS/JavaScript:

```python
def render_navbar(active_page: str = None):
    """Render navbar with hybrid HTML + Streamlit navigation"""
    
    # Inject sidebar hiding CSS
    hide_sidebar()
    
    # Render HTML navbar (visual only)
    st.markdown(navbar_html, unsafe_allow_html=True)
    
    # Hidden Streamlit buttons for navigation (in sidebar or hidden container)
    # These are triggered by JavaScript click events from HTML buttons
    if st.button("nav_landing", key="hidden_landing"):
        st.switch_page("pages/1_Landing.py")
    if st.button("nav_login", key="hidden_login"):
        st.switch_page("pages/2_Login.py")
    # ... more hidden buttons
```

**Recommended Approach**: 

Replace the HTML-based navbar with a **Streamlit-native navbar using st.columns() and custom styled st.button()** elements. This provides:
- Direct Python callback access for st.switch_page()
- Full control over styling via CSS
- No JavaScript workarounds needed
- Better compatibility with Streamlit's reactive model

### 3. CSS Injection Module

**Purpose**: Hide default sidebar and style custom navbar

**Implementation**:
```python
def hide_default_sidebar():
    """Inject CSS to completely hide Streamlit's default sidebar"""
    st.markdown("""
        <style>
        /* Hide default sidebar */
        [data-testid="stSidebar"] {
            display: none;
        }
        
        /* Remove sidebar collapse button */
        button[kind="header"] {
            display: none;
        }
        
        /* Adjust main content to full width */
        .main .block-container {
            max-width: 100%;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)
```

### 4. Page Modifications

Each page (Landing, Login, Signup, Dashboard) requires minimal changes:

**Changes Required**:
1. Remove any href-based links in page content
2. Replace with st.button() + st.switch_page() combinations
3. Ensure `hide_default_sidebar()` is called early in each page

**Example (pages/1_Landing.py)**:
```python
# Current:
st.markdown('<a href="/Login">Login</a>', unsafe_allow_html=True)

# New:
if st.button("Login", key="hero_login"):
    st.switch_page("pages/2_Login.py")
```

## Data Models

### Navigation State

No persistent state is required. Streamlit's multipage architecture handles page state internally.

**Transient State** (per-session):
- `st.session_state` may store user context (login status, filters, etc.) but navigation itself is stateless
- Each page switch clears temporary UI state (form inputs, button clicks)

**Page Path Mapping**:
```python
PAGE_PATHS = {
    "landing": "pages/1_Landing.py",
    "login": "pages/2_Login.py", 
    "signup": "pages/3_Signup.py",
    "dashboard": "pages/4_Dashboard.py"
}
```

### Error Handling Model

```python
def safe_navigate(page_path: str):
    """Navigate to page with error handling"""
    try:
        st.switch_page(page_path)
    except FileNotFoundError:
        st.error(f"Page not found: {page_path}")
        # Stay on current page
    except Exception as e:
        st.error(f"Navigation error: {str(e)}")
        # Log error for debugging
```

## Error Handling

### 1. Invalid Page Path

**Scenario**: st.switch_page() called with non-existent page path

**Handling**:
```python
try:
    st.switch_page("pages/5_NonExistent.py")
except FileNotFoundError as e:
    st.error("The requested page does not exist. Please contact support.")
    # Log error: logger.error(f"Navigation failed: {e}")
```

### 2. Sidebar CSS Not Applied

**Scenario**: CSS injection fails or is overridden

**Detection**: Check if sidebar is visible after CSS injection

**Handling**:
- Fall back to `st.set_page_config(initial_sidebar_state="collapsed")`
- Show warning to user: "Sidebar may be visible. Please collapse it manually."

### 3. Navigation During Form Submission

**Scenario**: User clicks navigation button while form is processing

**Handling**:
```python
if st.session_state.get('form_processing', False):
    st.warning("Please wait for the current operation to complete.")
    return

if st.button("Navigate"):
    st.session_state['form_processing'] = True
    st.switch_page("pages/X_Page.py")
```

### 4. Streamlit Version Compatibility

**Scenario**: st.switch_page() not available (Streamlit < 1.28.0)

**Detection**:
```python
import streamlit as st

if not hasattr(st, 'switch_page'):
    st.error("This application requires Streamlit >= 1.28.0. Please upgrade.")
    st.stop()
```

### 5. Page Initialization Errors

**Scenario**: Target page raises exception during load

**Handling**:
- Streamlit will catch and display error automatically
- Implement per-page error boundaries:

```python
# In each page
try:
    # Page content
    render_page()
except Exception as e:
    st.error("An error occurred loading this page.")
    st.exception(e)
    if st.button("Return to Home"):
        st.switch_page("pages/1_Landing.py")
```

## Testing Strategy

### Unit Testing

**Test Scope**: Individual functions and components

**Test Cases**:

1. **test_navbar_rendering**
   - Verify navbar HTML/components render without errors
   - Check all navigation buttons are present
   - Validate button keys are unique

2. **test_css_injection**
   - Verify hide_sidebar() generates valid CSS
   - Check CSS contains required selectors
   - Validate no syntax errors in CSS

3. **test_page_path_resolution**
   - Verify PAGE_PATHS mapping is correct
   - Check all paths point to existing files
   - Validate path format matches Streamlit requirements

**Test Framework**: pytest + streamlit-testing-library

```python
import pytest
from components.navbar import render_navbar, hide_default_sidebar

def test_hide_sidebar_css():
    """Test sidebar hiding CSS is valid"""
    # Mock st.markdown
    captured_css = []
    
    def mock_markdown(content, unsafe_allow_html=False):
        captured_css.append(content)
    
    # Execute
    hide_default_sidebar()
    
    # Assert
    assert len(captured_css) > 0
    assert '[data-testid="stSidebar"]' in captured_css[0]
    assert 'display: none' in captured_css[0]
```

### Integration Testing

**Test Scope**: Navigation flow between pages

**Test Cases**:

1. **test_app_redirects_to_landing**
   - Open app.py
   - Verify automatic redirect to Landing page
   - Check URL reflects Landing page

2. **test_navbar_navigation_landing_to_login**
   - Start on Landing page
   - Click Login button in navbar
   - Verify Login page loads
   - Check sidebar remains hidden

3. **test_navbar_navigation_all_pages**
   - Iterate through all pages
   - Click each navbar button from each page
   - Verify correct page loads each time

4. **test_sidebar_hidden_on_all_pages**
   - Visit each page (Landing, Login, Signup, Dashboard)
   - Check sidebar is not visible on any page
   - Verify main content uses full width

5. **test_login_form_navigation**
   - Fill out login form
   - Submit form
   - Verify navigation to Dashboard
   - Check form data handling during navigation

**Test Framework**: pytest + Selenium/Playwright for browser automation

```python
import pytest
from playwright.sync_api import Page, expect

def test_navbar_navigation(page: Page):
    """Test navigation from Landing to Login via navbar"""
    # Navigate to app
    page.goto("http://localhost:8501")
    
    # Should auto-redirect to Landing
    expect(page).to_have_url("http://localhost:8501/Landing")
    
    # Click Login button
    page.click('button:has-text("Login")')
    
    # Should navigate to Login page
    expect(page).to_have_url("http://localhost:8501/Login")
    
    # Sidebar should not be visible
    sidebar = page.query_selector('[data-testid="stSidebar"]')
    assert sidebar is None or not sidebar.is_visible()
```

### Manual Testing

**Test Scope**: Visual verification and user experience

**Test Cases**:

1. **Visual Consistency Check**
   - Navigate through all pages
   - Verify navbar design matches original
   - Check no visual regressions in page layouts

2. **Responsive Design Check**
   - Test on desktop (1920x1080, 1366x768)
   - Test on tablet (768x1024)
   - Test on mobile (375x667)
   - Verify navbar remains functional at all sizes

3. **Browser Compatibility Check**
   - Test on Chrome, Firefox, Safari, Edge
   - Verify navigation works consistently
   - Check CSS compatibility

4. **Accessibility Check**
   - Navigate using keyboard only (Tab, Enter)
   - Test with screen reader
   - Verify focus indicators are visible

**Test Checklist**:
- [ ] Default sidebar is hidden on all pages
- [ ] Navbar buttons trigger correct page transitions
- [ ] Landing page loads by default on app start
- [ ] All page designs remain unchanged
- [ ] Navigation works from every page to every other page
- [ ] Login form submission navigates to Dashboard
- [ ] Signup form submission navigates appropriately
- [ ] Browser back/forward buttons work correctly
- [ ] No console errors during navigation
- [ ] Page load performance is acceptable (<2s)

### Property-Based Testing

Property-based testing is **not applicable** for this feature because:

1. **UI Navigation is deterministic**: Navigation between specific pages follows fixed paths (Landing → Login, Login → Dashboard), not universal properties across arbitrary inputs
2. **State-based behavior**: Navigation behavior depends on UI state (which page, which button), not input transformation
3. **No data transformation logic**: No parsers, serializers, or algorithms that benefit from input randomization
4. **Integration-focused**: The feature tests integration between Streamlit components and browser behavior, better suited for example-based integration tests

**Alternative Testing Approach**: Use example-based integration tests with comprehensive coverage of all navigation paths (already specified above).

## Implementation Notes

### Key Considerations

1. **Streamlit Version Requirement**: Requires Streamlit >= 1.28.0 for st.switch_page() support
2. **CSS Specificity**: Sidebar hiding CSS must have sufficient specificity to override Streamlit's default styles
3. **Button Key Uniqueness**: All st.button() calls must have unique keys to avoid conflicts
4. **Page State Preservation**: st.switch_page() does not preserve session state between pages (by design)
5. **URL Synchronization**: Streamlit handles URL updates automatically when using st.switch_page()

### Performance Considerations

1. **Page Load Time**: Each st.switch_page() call triggers a full page reload
   - Mitigation: Keep page initialization code lightweight
   - Consider caching data loading with @st.cache_data

2. **CSS Injection**: Injecting CSS on every page load adds minimal overhead
   - Overhead: ~1-2ms per page load
   - Acceptable for this use case

3. **Button Rendering**: Using st.button() instead of HTML may slightly increase render time
   - Overhead: ~5-10ms for navbar with 6 buttons
   - Acceptable trade-off for proper functionality

### Migration Path

**Phase 1: Update app.py**
- Add st.switch_page() redirect to Landing

**Phase 2: Update navbar.py**
- Implement hide_default_sidebar()
- Replace href links with st.button() + st.switch_page()
- Apply custom CSS for styling

**Phase 3: Update pages**
- Replace href links in page content with navigation buttons
- Ensure all pages call hide_default_sidebar()

**Phase 4: Testing**
- Run unit tests
- Run integration tests
- Perform manual testing

**Phase 5: Deployment**
- Update requirements.txt (ensure Streamlit >= 1.28.0)
- Deploy to production
- Monitor for navigation errors

### Rollback Plan

If navigation changes cause critical issues:

1. **Revert navbar.py** to href-based version
2. **Revert app.py** to welcome message version  
3. **Remove hide_default_sidebar() calls** from all pages
4. **Keep sidebar visible** as fallback navigation

File-level changes are isolated to:
- app.py
- components/navbar.py
- Each page file (minimal changes)

All changes can be reverted via Git without data loss.

## Dependencies

### Required Libraries
- `streamlit >= 1.28.0` (for st.switch_page() API)
- All existing dependencies (pandas, plotly, etc.) remain unchanged

### Python Version
- Python >= 3.8 (existing requirement)

### Browser Requirements
- Modern browsers with CSS3 support (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)
- JavaScript enabled (for Streamlit functionality)

## Security Considerations

### 1. Client-Side Navigation
- Navigation is handled client-side by Streamlit
- No server-side validation of page access
- **Recommendation**: Implement authentication checks at the page level (not in scope for this feature)

### 2. CSS Injection
- CSS is injected via `st.markdown(unsafe_allow_html=True)`
- Content is static and controlled (no user input)
- **Risk**: Low - no XSS vulnerability as CSS content is not user-provided

### 3. Page Access Control
- Currently, all pages are publicly accessible
- st.switch_page() does not enforce access control
- **Recommendation**: Add authentication middleware (future enhancement)

### 4. URL Manipulation
- Users can manually navigate to pages by URL (e.g., `/Login`, `/Dashboard`)
- Streamlit's router handles URL mapping
- **Risk**: Low - same behavior as current implementation

## Appendix

### Streamlit Multipage Architecture Reference

Streamlit's multipage app structure:
- Main file: `app.py` (entry point)
- Page files: `pages/X_PageName.py` (X is optional numeric prefix for ordering)
- Automatic routing: Streamlit generates routes from page filenames
- Default sidebar: Auto-generated navigation menu (to be hidden in our solution)

**Page Naming Convention**:
- `1_Landing.py` → Route: `/Landing`
- `2_Login.py` → Route: `/Login`
- `3_Signup.py` → Route: `/Signup`
- `4_Dashboard.py` → Route: `/Dashboard`

### st.switch_page() API Reference

```python
st.switch_page(page: str) -> None
```

**Parameters**:
- `page` (str): Relative path to page file from project root
  - Example: `"pages/1_Landing.py"`
  - Example: `"pages/2_Login.py"`

**Behavior**:
- Triggers immediate navigation to specified page
- Updates browser URL to match page route
- Resets page execution context (reruns target page script)
- Does not preserve local variables (use st.session_state for persistence)

**Exceptions**:
- `FileNotFoundError`: Raised if page file doesn't exist
- `StreamlitAPIException`: Raised if called outside valid Streamlit context

### CSS Selectors for Sidebar Hiding

```css
/* Primary selector - hides sidebar container */
[data-testid="stSidebar"] {
    display: none;
}

/* Secondary selector - hides collapse button */
[data-testid="collapsedControl"] {
    display: none;
}

/* Tertiary selector - hides sidebar backdrop on mobile */
[data-testid="stSidebarNav"] {
    display: none;
}

/* Adjust main content width */
.main .block-container {
    max-width: 100%;
    padding-left: 2rem;
    padding-right: 2rem;
}
```

### Example: Complete navbar.py Implementation

```python
"""
Intelligent Software Defect Tracking System with Resolution Assistance - Navigation Component
Provides reusable navigation bar for all pages with st.switch_page() navigation.
"""

import streamlit as st


def hide_default_sidebar():
    """Inject CSS to completely hide Streamlit's default sidebar"""
    st.markdown("""
        <style>
        /* Hide default sidebar */
        [data-testid="stSidebar"] {
            display: none;
        }
        
        /* Hide sidebar collapse button */
        [data-testid="collapsedControl"] {
            display: none;
        }
        
        /* Hide sidebar nav */
        [data-testid="stSidebarNav"] {
            display: none;
        }
        
        /* Adjust main content to full width */
        .main .block-container {
            max-width: 100%;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        
        /* Custom navbar button styling */
        .navbar-button {
            background: transparent;
            border: none;
            color: white;
            padding: 0.75rem 1.1rem;
            border-radius: 999px;
            cursor: pointer;
            transition: all 0.25s ease;
            font-size: 1rem;
        }
        
        .navbar-button:hover {
            background: rgba(255, 255, 255, 0.1);
        }
        
        .navbar-button-primary {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.14);
        }
        
        .navbar-button-primary:hover {
            background: rgba(255, 255, 255, 0.15);
        }
        
        .navbar-button-cta {
            background-color: #F87171;
            box-shadow: 0 14px 34px rgba(220, 38, 38, 0.35);
        }
        
        .navbar-button-cta:hover {
            background-color: #EF4444;
        }
        </style>
    """, unsafe_allow_html=True)


def render_navbar(active_page: str = None):
    """
    Render the navigation bar component with st.switch_page() navigation.
    
    Args:
        active_page: Name of the currently active page ('landing', 'login', 'signup', 'dashboard')
    """
    # Hide default sidebar
    hide_default_sidebar()
    
    # Render navbar container HTML
    st.markdown("""
    <nav style="position: sticky; top: 1rem; z-index: 1100; padding: 1.1rem 2rem; margin: 0 auto 1rem auto; max-width: 1450px; width: calc(100% - 1.5rem); border-radius: 28px; background: rgba(15, 23, 42, 0.94); border: 1px solid rgba(239, 68, 68, 0.45); box-shadow: 0 30px 60px rgba(0, 0, 0, 0.35);">
    </nav>
    """, unsafe_allow_html=True)
    
    # Create navbar layout with columns
    cols = st.columns([1, 6, 2])
    
    with cols[0]:
        # Home icon button
        if st.button("🐛", key="nav_icon", help="Home"):
            st.switch_page("pages/1_Landing.py")
    
    with cols[1]:
        # Navigation links
        nav_cols = st.columns(4)
        
        with nav_cols[0]:
            if st.button("Home", key="nav_home"):
                st.switch_page("pages/1_Landing.py")
        
        with nav_cols[1]:
            # Anchor link (stays on Landing page)
            st.markdown('<a href="#lifecycle" style="padding: 0.75rem 1.1rem; border-radius: 999px; color: white; text-decoration: none;">Defect Tracking</a>', unsafe_allow_html=True)
        
        with nav_cols[2]:
            # Anchor link (stays on Landing page)
            st.markdown('<a href="#features" style="padding: 0.75rem 1.1rem; border-radius: 999px; color: white; text-decoration: none;">Features</a>', unsafe_allow_html=True)
        
        with nav_cols[3]:
            # Anchor link (stays on Landing page)
            st.markdown('<a href="#why-us" style="padding: 0.75rem 1.1rem; border-radius: 999px; color: white; text-decoration: none;">Why Choose Us</a>', unsafe_allow_html=True)
    
    with cols[2]:
        # Action buttons
        action_cols = st.columns(2)
        
        with action_cols[0]:
            if st.button("Login", key="nav_login", type="secondary"):
                st.switch_page("pages/2_Login.py")
        
        with action_cols[1]:
            if st.button("Sign Up", key="nav_signup", type="primary"):
                st.switch_page("pages/3_Signup.py")
```

This implementation provides a functional navbar with proper navigation while maintaining as much of the original styling as possible through CSS injection.
