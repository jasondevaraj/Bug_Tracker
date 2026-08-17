"""
Intelligent Software Defect Tracking System with Resolution Assistance - Data Loading Utilities
Provides CSV loading, cleaning, and preprocessing functions.
"""

import pandas as pd
import streamlit as st
from pathlib import Path
from datetime import datetime


# Date columns to parse
DATE_FIELDS = [
    'Date_Reported',
    'Date_Assigned',
    'Date_Fixed',
    'Date_Retested',
    'Date_Closed'
]

# Numeric columns to coerce
NUMERIC_FIELDS = [
    'Resolution_Time_Hours',
    'Similarity_Score'
]

# Categorical columns to trim
CATEGORICAL_FIELDS = [
    'Sprint', 'Release_Version', 'Module', 'Feature', 'Component',
    'Severity', 'Priority', 'Status', 'Resolution', 'Root_Cause',
    'Assigned_To', 'Team', 'Bug_Type', 'Reporter', 'QA_Engineer',
    'Environment', 'Operating_System', 'Browser', 'Device',
    'Lifecycle_Stage'
]


@st.cache_data(ttl=3600)
def load_csv(csv_path: str = None) -> pd.DataFrame:
    """
    Load and parse the CSV file with caching.
    
    Args:
        csv_path: Path to CSV file. If None, uses default path.
        
    Returns:
        Cleaned DataFrame
        
    Raises:
        FileNotFoundError: If CSV file doesn't exist
        Exception: If CSV parsing fails
    """
    if csv_path is None:
        # Default path relative to project root
        base_path = Path(__file__).parent.parent
        csv_path = base_path / 'data' / 'Bug_Life_Cycle_Managementreport.csv'
    
    csv_path = Path(csv_path)
    
    if not csv_path.exists():
        raise FileNotFoundError(
            f"CSV file not found at: {csv_path}\n"
            f"Please ensure the dataset exists in the data/ directory."
        )
    
    try:
        # Load CSV with pandas
        df = pd.read_csv(csv_path)
        
        # Clean the data
        df = clean_dataframe(df)
        
        return df
        
    except Exception as e:
        raise Exception(f"Failed to load CSV: {str(e)}")


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and preprocess the dataframe.
    
    Args:
        df: Raw dataframe from CSV
        
    Returns:
        Cleaned dataframe
    """
    df = df.copy()
    
    # Parse date columns
    for field in DATE_FIELDS:
        if field in df.columns:
            df[field] = pd.to_datetime(df[field], errors='coerce')
    
    # Coerce numeric columns
    for field in NUMERIC_FIELDS:
        if field in df.columns:
            df[field] = pd.to_numeric(df[field], errors='coerce').fillna(0)
    
    # Trim categorical strings
    for field in CATEGORICAL_FIELDS:
        if field in df.columns:
            df[field] = df[field].astype(str).str.strip()
    
    return df


def get_unique_values(df: pd.DataFrame, field: str) -> list:
    """
    Get sorted unique values for a given field.
    Used for populating filter dropdowns.
    
    Args:
        df: DataFrame
        field: Column name
        
    Returns:
        Sorted list of unique values
    """
    if field not in df.columns:
        return []
    
    values = df[field].dropna().unique()
    return sorted([str(v) for v in values if str(v).strip()])


def filter_dataframe(df: pd.DataFrame, filters: dict) -> pd.DataFrame:
    """
    Apply filters to the dataframe.
    
    Args:
        df: DataFrame to filter
        filters: Dictionary of field: value pairs
        
    Returns:
        Filtered DataFrame
    """
    filtered_df = df.copy()
    
    for field, value in filters.items():
        if value and field in filtered_df.columns:
            # Handle search query separately (searches Bug_ID and Bug_Title)
            if field == 'searchQuery':
                mask = (
                    filtered_df['Bug_ID'].astype(str).str.contains(value, case=False, na=False) |
                    filtered_df['Bug_Title'].astype(str).str.contains(value, case=False, na=False)
                )
                filtered_df = filtered_df[mask]
            else:
                # Exact match for dropdown filters
                filtered_df = filtered_df[filtered_df[field] == value]
    
    return filtered_df
