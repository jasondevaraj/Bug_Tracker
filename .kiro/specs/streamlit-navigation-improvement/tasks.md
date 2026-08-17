# Implementation Plan: Streamlit Navigation Improvement

## Overview

This plan implements navigation improvements for the Intelligent Software Defect Tracking System with Resolution Assistance by hiding the default Streamlit sidebar, replacing href-based navigation with `st.switch_page()`, and making the Landing page the default entry point. The implementation focuses solely on navigation mechanisms while preserving all existing page designs, layouts, and styling.

## Tasks

- [ ] 1. Create CSS sidebar hiding utility
  - [ ] 1.1 Implement hide_default_sidebar() function in components/navbar.py
    - Add CSS injection function to hide Streamlit's default sidebar
    - Target `[data-testid="stSidebar"]`, `[data-testid="collapsedControl"]`, and `[data-testid="stSidebarNav"]` selectors
    - Adjust main content width to utilize full viewport
    - Include CSS for navbar button styling (navbar-button, navbar-button-primary, navbar-button-cta classes)
    - _Requirements: 1.1, 1.2, 1.3, 1.4_

- [ ] 2. Implement st.switch_page() navigation in navbar component
  - [ ] 2.1 Replace href-based navbar with Streamlit button-based navigation
    - Remove HTML navbar structure with hardcoded href links (`/Login`, `/Signup`)
    - Implement navbar using `st.columns()` layout with three sections: icon, navigation links, action buttons
    - Add `st.button()` for Home icon (🐛) that calls `st.switch_page("pages/1_Landing.py")`
    - Add `st.button()` for "Home" link that calls `st.switch_page("pages/1_Landing.py")`
    - Keep anchor links for Defect Tracking, Features, Why Choose Us (they stay on Landing page)
    - Add `st.button()` for "Login" that calls `st.switch_page("pages/2_Login.py")`
    - Add `st.button()` for "Sign Up" that calls `st.switch_page("pages/3_Signup.py")`
    - Ensure all button keys are unique (nav_icon, nav_home, nav_login, nav_signup)
    - Call `hide_default_sidebar()` at the start of render_navbar()
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 4.1, 4.2, 5.1, 5.2, 6.1, 6.2, 9.1, 9.2, 9.3, 9.4, 11.1, 11.2_

- [ ] 3. Update app.py entry point to redirect to Landing page
  - [ ] 3.1 Replace welcome content with st.switch_page() redirect
    - Remove all st.markdown() welcome message content
    - Add immediate redirect to Landing page using `st.switch_page("pages/1_Landing.py")`
    - Keep page configuration and theme application
    - _Requirements: 2.1, 2.2, 2.3_

- [ ] 4. Update Landing page navigation links
  - [ ] 4.1 Replace href-based navigation with st.button() + st.switch_page()
    - Replace hero section "Get Started" href link with `st.button()` + `st.switch_page("pages/3_Signup.py")`
    - Replace hero section "Login" href link with `st.button()` + `st.switch_page("pages/2_Login.py")`
    - Replace CTA section "Sign Up Now" href link with `st.button()` + `st.switch_page("pages/3_Signup.py")`
    - Replace CTA section "Login" href link with `st.button()` + `st.switch_page("pages/2_Login.py")`
    - Ensure all button keys are unique (hero_signup, hero_login, cta_signup, cta_login)
    - _Requirements: 4.2, 5.2, 6.2, 7.2, 10.1, 11.1, 11.2, 11.3_

- [ ] 5. Update Login page navigation links
  - [ ] 5.1 Replace href-based navigation with st.button() + st.switch_page()
    - Replace logo home link (href="/") with `st.button()` + `st.switch_page("pages/1_Landing.py")`
    - Replace "Sign Up" link (href="/Signup") with inline text + `st.button()` that calls `st.switch_page("pages/3_Signup.py")`
    - Update form submission to navigate to Dashboard using existing `st.switch_page("pages/4_Dashboard.py")` (already implemented)
    - Ensure all button keys are unique (login_home, login_to_signup)
    - _Requirements: 4.2, 6.2, 7.2, 10.2, 11.1, 11.2, 11.3_

- [ ] 6. Update Signup page navigation links
  - [ ] 6.1 Replace href-based navigation with st.button() + st.switch_page()
    - Replace logo home link (href="/") with `st.button()` + `st.switch_page("pages/1_Landing.py")`
    - Replace "Login" link (href="/Login") with inline text + `st.button()` that calls `st.switch_page("pages/2_Login.py")`
    - Update form submission to navigate to Login using existing `st.switch_page("pages/2_Login.py")` (already implemented)
    - Ensure all button keys are unique (signup_home, signup_to_login)
    - _Requirements: 5.2, 6.2, 7.2, 10.3, 11.1, 11.2, 11.3_

- [ ] 7. Update Dashboard page navigation links
  - [ ] 7.1 Replace href-based footer navigation with st.button() + st.switch_page()
    - Replace footer "Home" link (href="/") with `st.button()` + `st.switch_page("pages/1_Landing.py")`
    - Replace footer "Landing" link (href="/Landing") with `st.button()` + `st.switch_page("pages/1_Landing.py")`
    - Replace footer "Login" link (href="/Login") with `st.button()` + `st.switch_page("pages/2_Login.py")`
    - Ensure all button keys are unique (dashboard_footer_home, dashboard_footer_landing, dashboard_footer_login)
    - _Requirements: 4.2, 5.2, 7.2, 10.4, 11.1, 11.2, 11.3_

- [ ] 8. Add error handling for navigation
  - [ ] 8.1 Wrap st.switch_page() calls in try-except blocks
    - Add error handling wrapper function `safe_navigate(page_path: str)` in components/navbar.py
    - Catch `FileNotFoundError` and display user-friendly error message
    - Catch generic `Exception` and log error while keeping user on current page
    - Apply error handling to all navigation calls in navbar, pages, and app.py
    - _Requirements: 12.1, 12.2, 12.3_

- [ ] 9. Checkpoint - Verify navigation functionality
  - Ensure all tests pass, ask the user if questions arise.

- [ ]* 10. Write integration tests for navigation flow
  - [ ]* 10.1 Test app.py redirects to Landing page
    - Verify opening app.py automatically loads Landing page
    - _Requirements: 2.1, 2.2_
  
  - [ ]* 10.2 Test navbar navigation from each page
    - Test Home button navigates to Landing from all pages
    - Test Login button navigates to Login page from all pages
    - Test Sign Up button navigates to Signup page from all pages
    - _Requirements: 3.1, 4.1, 5.1, 6.1_
  
  - [ ]* 10.3 Test sidebar remains hidden across all pages
    - Verify sidebar is not visible on Landing, Login, Signup, Dashboard pages
    - Check `[data-testid="stSidebar"]` element is hidden
    - _Requirements: 1.1, 1.2, 1.3, 1.4_
  
  - [ ]* 10.4 Test form submission navigation
    - Test Login form navigates to Dashboard on submission
    - Test Signup form navigates to Login page on submission
    - _Requirements: 7.1, 7.2, 11.3_

- [ ] 11. Final checkpoint and verification
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster implementation
- The design document uses Python (Streamlit framework), so all implementation will be in Python
- All existing page designs, layouts, and styling will be preserved - only navigation mechanism changes
- No property-based tests are needed (UI navigation is deterministic and state-based)
- Integration tests verify navigation paths work correctly across all pages
- Checkpoints ensure incremental validation of navigation functionality
- Each task references specific requirements for traceability

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1"] },
    { "id": 1, "tasks": ["2.1", "3.1"] },
    { "id": 2, "tasks": ["4.1", "5.1", "6.1", "7.1"] },
    { "id": 3, "tasks": ["8.1"] },
    { "id": 4, "tasks": ["10.1", "10.2", "10.3", "10.4"] }
  ]
}
```
