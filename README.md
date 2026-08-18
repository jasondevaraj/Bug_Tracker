# Intelligent Software Defect Tracking System with Resolution Assistance

## Overview

The **Intelligent Software Defect Tracking System with Resolution Assistance** is a data-driven application designed to help software development and testing teams manage, analyze, and understand software defects efficiently.

The system centralizes defect information and provides an interactive dashboard for searching, filtering, and analyzing defects across releases, sprints, modules, teams, priorities, severity levels, and environments.

## Project Objectives

- Centralize software defect information.
- Track defects across releases, sprints, modules, teams, and environments.
- Monitor defect status, priority, severity, and other important attributes.
- Provide interactive filtering and search functionality.
- Generate meaningful defect analytics and visualizations.
- Perform data preprocessing and historical defect analysis.
- Provide insights that can support more efficient defect management.

## Key Features

- Interactive Streamlit dashboard
- Defect search and filtering
- Release and sprint-based analysis
- Module-wise defect analysis
- Priority and severity analysis
- Bug status distribution
- Team-wise average resolution time
- Weekly bug reporting trends
- Resolution type analysis
- Root cause analysis

## Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **Plotly**
- **Scikit-learn**
- **Git & GitHub**

## Machine Learning

The project includes data preprocessing and experimentation with different machine learning approaches for defect-related prediction tasks.

The approaches explored include:

- Support Vector Machine (SVM)
- Linear Regression
- Decision Tree-based models
- Random Forest classification

These techniques are explored to support the prediction of defect priority and resolution-assistance related analysis.

## Dashboard Analytics

The dashboard provides visualizations for:

1. Bug Status Distribution
2. Bugs by Severity
3. Bugs by Module and Status
4. Bugs by Priority
5. Average Resolution Time by Team
6. Weekly Bug Reporting Trend
7. Resolution Type
8. Root Cause Analysis

## Installation

### 1. Clone the Repository

git clone <your-github-repository-url>
cd Intelligent-software-defect-tracking-system-with-resolution-assistance

### 2. Create and Activate Virtual Environment

python -m venv .venv

**Windows:**
.venv\Scripts\activate

**Linux/macOS:**
source .venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run the Application

streamlit run app.py

Open the local URL provided by Streamlit in your browser.

## Project Structure

```text
Intelligent-software-defect-tracking-system-with-resolution-assistance/
│
├── .kiro/
├── .streamlit/
├── .vscode/
│
├── assets/
│   ├── css/
│   ├── icons/
│   └── images/
│
├── components/
│
├── data/
│   └── Bug_Life_Cycle_Managementreport.csv
│
├── html_reference/
│   ├── Bug-Lifecycle-Dashboard/
│   └── Bug-Lifecycle-Landing/
│
├── pages/
│   ├── 1_landing.py
│   ├── 2_Login.py
│   ├── 3_Signup.py
│   └── 4_Dashboard.py
│
├── utils/
│
├── .gitignore
├── app.py
├── implementation_plan.md
├── LICENSE
└── requirements.txt
