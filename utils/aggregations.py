"""
Bug Lifecycle Management System - Data Aggregation Utilities
Provides data transformation and aggregation functions for dashboard charts.
"""

import pandas as pd
from typing import Dict, List, Tuple


def count_by(df: pd.DataFrame, field: str) -> Dict[str, int]:
    """
    Count occurrences of each unique value in a given field.
    
    Args:
        df: DataFrame
        field: Column name to count
        
    Returns:
        Dictionary mapping values to counts
    """
    if field not in df.columns:
        return {}
    
    counts = df[field].fillna('Unknown').value_counts().to_dict()
    return counts


def group_by(df: pd.DataFrame, field: str) -> Dict[str, pd.DataFrame]:
    """
    Group rows by a field value.
    
    Args:
        df: DataFrame
        field: Column name to group by
        
    Returns:
        Dictionary mapping values to DataFrames
    """
    if field not in df.columns:
        return {}
    
    df_copy = df.copy()
    df_copy[field] = df_copy[field].fillna('Unknown')
    
    groups = {name: group for name, group in df_copy.groupby(field)}
    return groups


def average_by(df: pd.DataFrame, numeric_field: str, group_field: str = None) -> float | Dict[str, float]:
    """
    Compute average of a numeric field, optionally grouped by a category.
    
    Args:
        df: DataFrame
        numeric_field: Column to average
        group_field: Optional column to group by
        
    Returns:
        Single average value or dictionary of group: average
    """
    if numeric_field not in df.columns:
        return 0.0 if group_field is None else {}
    
    # Filter out zero/null values
    valid_data = df[df[numeric_field] > 0]
    
    if group_field is None:
        # Return single average
        return valid_data[numeric_field].mean() if len(valid_data) > 0 else 0.0
    
    if group_field not in df.columns:
        return {}
    
    # Group and compute averages
    result = {}
    for name, group in valid_data.groupby(group_field):
        avg = group[numeric_field].mean()
        result[str(name)] = round(avg, 1)
    
    return result


def time_series_by(df: pd.DataFrame, date_field: str, granularity: str = 'week') -> Tuple[List[str], List[int]]:
    """
    Aggregate count by a date field at weekly or daily granularity.
    
    Args:
        df: DataFrame
        date_field: Date column name
        granularity: 'week' or 'day'
        
    Returns:
        Tuple of (labels, values) for time series
    """
    if date_field not in df.columns:
        return ([], [])
    
    # Filter valid dates
    valid_data = df[df[date_field].notna()].copy()
    
    if len(valid_data) == 0:
        return ([], [])
    
    valid_data = valid_data.sort_values(date_field)
    
    if granularity == 'day':
        # Daily aggregation
        valid_data['date_key'] = valid_data[date_field].dt.date
        counts = valid_data.groupby('date_key').size()
        
        labels = [d.strftime('%b %d') for d in counts.index]
        values = counts.tolist()
        
    else:
        # Weekly aggregation (default)
        # Set to Monday of each week
        valid_data['week_start'] = valid_data[date_field].dt.to_period('W').apply(lambda r: r.start_time)
        counts = valid_data.groupby('week_start').size()
        
        labels = [d.strftime('%b %d') for d in counts.index]
        values = counts.tolist()
    
    return (labels, values)


def stacked_count_by(df: pd.DataFrame, group_field: str, stack_field: str) -> Tuple[List[str], List[Dict]]:
    """
    Build a stacked dataset: for each category in group_field,
    count how many rows fall into each value of stack_field.
    
    Args:
        df: DataFrame
        group_field: Field to group by (x-axis)
        stack_field: Field to stack by (legend)
        
    Returns:
        Tuple of (labels, datasets) where datasets is list of {label, data} dicts
    """
    if group_field not in df.columns or stack_field not in df.columns:
        return ([], [])
    
    df_copy = df.copy()
    df_copy[group_field] = df_copy[group_field].fillna('Unknown')
    df_copy[stack_field] = df_copy[stack_field].fillna('Unknown')
    
    # Get unique values for stacking
    stack_values = sorted(df_copy[stack_field].unique())
    labels = sorted(df_copy[group_field].unique())
    
    # Build datasets
    datasets = []
    for stack_val in stack_values:
        data = []
        for label in labels:
            count = len(df_copy[(df_copy[group_field] == label) & (df_copy[stack_field] == stack_val)])
            data.append(count)
        
        datasets.append({
            'label': str(stack_val),
            'data': data
        })
    
    return (labels, datasets)


def compute_kpis(df: pd.DataFrame) -> Dict[str, int | float]:
    """
    Compute KPI summary metrics for dashboard.
    
    Args:
        df: DataFrame
        
    Returns:
        Dictionary of KPI values
    """
    total = len(df)
    open_bugs = len(df[df['Status'] == 'Open']) if 'Status' in df.columns else 0
    closed_bugs = len(df[df['Status'] == 'Closed']) if 'Status' in df.columns else 0
    critical_bugs = len(df[df['Severity'] == 'Critical']) if 'Severity' in df.columns else 0
    
    # Average resolution time
    if 'Resolution_Time_Hours' in df.columns:
        avg_resolution = df[df['Resolution_Time_Hours'] > 0]['Resolution_Time_Hours'].mean()
        avg_resolution = float(round(avg_resolution, 1)) if pd.notna(avg_resolution) else 0.0
    else:
        avg_resolution = 0.0
    
    return {
        'total': total,
        'openBugs': open_bugs,
        'closedBugs': closed_bugs,
        'criticalBugs': critical_bugs,
        'avgResolution': avg_resolution
    }
