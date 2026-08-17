"""
Intelligent Software Defect Tracking System with Resolution Assistance - Chart Components
Provides 8 Plotly chart rendering functions for the dashboard.
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from typing import Dict, List


def render_status_doughnut(df: pd.DataFrame):
    """
    Render Bug Status Distribution doughnut chart.
    
    Args:
        df: Filtered DataFrame
    """
    from utils.aggregations import count_by
    
    counts = count_by(df, 'Status')
    if not counts:
        st.info("No data available for status distribution")
        return
    
    labels = list(counts.keys())
    values = list(counts.values())
    
    colors = ['#F87171', '#EF4444', '#F97316', '#FBBF24', '#22C55E', '#38BDF8', '#A78BFA']
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.65,
        marker=dict(
            colors=colors[:len(labels)],
            line=dict(color='#111827', width=3)
        ),
        hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>',
        textposition='auto',
        textinfo='percent+label'
    )])
    
    fig.update_layout(
        title=dict(
            text='Bug Status Distribution',
            font=dict(size=18, color='#F8FAFC', family='Poppins'),
            x=0.5,
            xanchor='center'
        ),
        paper_bgcolor='rgba(15, 23, 42, 0.8)',
        plot_bgcolor='rgba(15, 23, 42, 0.8)',
        font=dict(family='Inter', color='#94A3B8'),
        showlegend=True,
        legend=dict(
            orientation='v',
            yanchor='middle',
            y=0.5,
            xanchor='left',
            x=1.02,
            font=dict(color='#94A3B8')
        ),
        height=400,
        margin=dict(t=60, b=20, l=20, r=120)
    )
    
    st.plotly_chart(fig, use_container_width=True, key='chart_status')


def render_severity_bar(df: pd.DataFrame):
    """
    Render Bugs by Severity horizontal bar chart.
    
    Args:
        df: Filtered DataFrame
    """
    from utils.aggregations import count_by
    
    counts = count_by(df, 'Severity')
    if not counts:
        st.info("No data available for severity distribution")
        return
    
    order = ['Critical', 'High', 'Medium', 'Low']
    labels = [s for s in order if s in counts]
    values = [counts[l] for l in labels]
    colors = ['#DC2626', '#F87171', '#F97316', '#FBBF24']
    
    fig = go.Figure(data=[go.Bar(
        x=values,
        y=labels,
        orientation='h',
        marker=dict(
            color=colors[:len(labels)],
            line=dict(color=colors[:len(labels)], width=1),
            opacity=0.85
        ),
        hovertemplate='<b>%{y}</b><br>Count: %{x}<extra></extra>',
        text=values,
        textposition='auto'
    )])
    
    fig.update_layout(
        title=dict(
            text='Bugs by Severity',
            font=dict(size=18, color='#F8FAFC', family='Poppins'),
            x=0.5,
            xanchor='center'
        ),
        paper_bgcolor='rgba(15, 23, 42, 0.8)',
        plot_bgcolor='rgba(15, 23, 42, 0.8)',
        font=dict(family='Inter', color='#94A3B8'),
        xaxis=dict(
            showgrid=True,
            gridcolor='rgba(255, 255, 255, 0.04)',
            zeroline=True
        ),
        yaxis=dict(showgrid=False),
        height=350,
        margin=dict(t=60, b=40, l=80, r=40),
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True, key='chart_severity')


def render_module_status_stacked(df: pd.DataFrame):
    """
    Render Bugs by Module × Status stacked bar chart.
    
    Args:
        df: Filtered DataFrame
    """
    from utils.aggregations import stacked_count_by
    
    labels, datasets = stacked_count_by(df, 'Module', 'Status')
    if not labels or not datasets:
        st.info("No data available for module × status")
        return
    
    colors = ['#F87171', '#EF4444', '#F97316', '#FBBF24', '#22C55E', '#38BDF8', '#A78BFA', '#F472B6']
    
    fig = go.Figure()
    
    for i, dataset in enumerate(datasets):
        fig.add_trace(go.Bar(
            name=dataset['label'],
            x=labels,
            y=dataset['data'],
            marker=dict(
                color=colors[i % len(colors)],
                line=dict(color=colors[i % len(colors)], width=1),
                opacity=0.85
            ),
            hovertemplate='<b>%{x}</b><br>' + dataset['label'] + ': %{y}<extra></extra>'
        ))
    
    fig.update_layout(
        title=dict(
            text='Bugs by Module & Status',
            font=dict(size=18, color='#F8FAFC', family='Poppins'),
            x=0.5,
            xanchor='center'
        ),
        barmode='stack',
        paper_bgcolor='rgba(15, 23, 42, 0.8)',
        plot_bgcolor='rgba(15, 23, 42, 0.8)',
        font=dict(family='Inter', color='#94A3B8'),
        xaxis=dict(
            showgrid=False,
            tickangle=-30
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(255, 255, 255, 0.04)',
            zeroline=True
        ),
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='center',
            x=0.5,
            font=dict(color='#94A3B8')
        ),
        height=400,
        margin=dict(t=100, b=60, l=60, r=40)
    )
    
    st.plotly_chart(fig, use_container_width=True, key='chart_module_status')


def render_priority_bar(df: pd.DataFrame):
    """
    Render Bugs by Priority bar chart.
    
    Args:
        df: Filtered DataFrame
    """
    from utils.aggregations import count_by
    
    counts = count_by(df, 'Priority')
    if not counts:
        st.info("No data available for priority distribution")
        return
    
    order = ['P1', 'P2', 'P3', 'P4']
    labels = [p for p in order if p in counts]
    values = [counts[l] for l in labels]
    colors = ['#EF4444', '#F87171', '#F97316', '#FBBF24']
    
    fig = go.Figure(data=[go.Bar(
        x=labels,
        y=values,
        marker=dict(
            color=colors[:len(labels)],
            line=dict(color=colors[:len(labels)], width=1),
            opacity=0.85
        ),
        hovertemplate='<b>%{x}</b><br>Count: %{y}<extra></extra>',
        text=values,
        textposition='auto'
    )])
    
    fig.update_layout(
        title=dict(
            text='Bugs by Priority',
            font=dict(size=18, color='#F8FAFC', family='Poppins'),
            x=0.5,
            xanchor='center'
        ),
        paper_bgcolor='rgba(15, 23, 42, 0.8)',
        plot_bgcolor='rgba(15, 23, 42, 0.8)',
        font=dict(family='Inter', color='#94A3B8'),
        xaxis=dict(showgrid=False),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(255, 255, 255, 0.04)',
            zeroline=True
        ),
        height=350,
        margin=dict(t=60, b=40, l=60, r=40),
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True, key='chart_priority')


def render_resolution_by_team(df: pd.DataFrame):
    """
    Render Average Resolution Time by Team bar chart.
    
    Args:
        df: Filtered DataFrame
    """
    from utils.aggregations import average_by
    
    avgs = average_by(df, 'Resolution_Time_Hours', 'Team')
    if not avgs:
        st.info("No data available for resolution time by team")
        return
    
    labels = sorted(avgs.keys())
    values = [round(avgs[l], 1) for l in labels]
    
    colors = ['#F87171', '#EF4444', '#F97316', '#FBBF24', '#22C55E', '#38BDF8', '#A78BFA']
    
    fig = go.Figure(data=[go.Bar(
        x=labels,
        y=values,
        marker=dict(
            color=colors[:len(labels)],
            line=dict(color=colors[:len(labels)], width=1),
            opacity=0.85
        ),
        hovertemplate='<b>%{x}</b><br>Avg Hours: %{y}<extra></extra>',
        text=values,
        textposition='auto'
    )])
    
    fig.update_layout(
        title=dict(
            text='Avg Resolution Time by Team',
            font=dict(size=18, color='#F8FAFC', family='Poppins'),
            x=0.5,
            xanchor='center'
        ),
        paper_bgcolor='rgba(15, 23, 42, 0.8)',
        plot_bgcolor='rgba(15, 23, 42, 0.8)',
        font=dict(family='Inter', color='#94A3B8'),
        xaxis=dict(showgrid=False),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(255, 255, 255, 0.04)',
            zeroline=True,
            title=dict(text='Hours', font=dict(color='#94A3B8'))
        ),
        height=350,
        margin=dict(t=60, b=40, l=60, r=40),
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True, key='chart_resolution_team')


def render_trend_line(df: pd.DataFrame):
    """
    Render Bug Reporting Trend line chart (weekly aggregation).
    
    Args:
        df: Filtered DataFrame
    """
    from utils.aggregations import time_series_by
    
    labels, values = time_series_by(df, 'Date_Reported', 'week')
    if not labels or not values:
        st.info("No data available for bug reporting trend")
        return
    
    fig = go.Figure(data=[go.Scatter(
        x=labels,
        y=values,
        mode='lines+markers',
        line=dict(color='#F87171', width=3, shape='spline'),
        fill='tozeroy',
        fillcolor='rgba(248, 113, 113, 0.12)',
        marker=dict(
            color='#F87171',
            size=8,
            line=dict(color='#111827', width=2)
        ),
        hovertemplate='<b>%{x}</b><br>Bugs Reported: %{y}<extra></extra>'
    )])
    
    fig.update_layout(
        title=dict(
            text='Bug Reporting Trend (Weekly)',
            font=dict(size=18, color='#F8FAFC', family='Poppins'),
            x=0.5,
            xanchor='center'
        ),
        paper_bgcolor='rgba(15, 23, 42, 0.8)',
        plot_bgcolor='rgba(15, 23, 42, 0.8)',
        font=dict(family='Inter', color='#94A3B8'),
        xaxis=dict(
            showgrid=False,
            tickangle=-30
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(255, 255, 255, 0.04)',
            zeroline=True,
            title=dict(text='Count', font=dict(color='#94A3B8'))
        ),
        height=350,
        margin=dict(t=60, b=60, l=60, r=40),
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True, key='chart_trend')


def render_resolution_pie(df: pd.DataFrame):
    """
    Render Resolution Type Distribution pie chart.
    
    Args:
        df: Filtered DataFrame
    """
    from utils.aggregations import count_by
    
    counts = count_by(df, 'Resolution')
    if not counts:
        st.info("No data available for resolution type")
        return
    
    labels = list(counts.keys())
    values = list(counts.values())
    
    colors = ['#F87171', '#EF4444', '#F97316', '#FBBF24', '#22C55E', '#38BDF8', '#A78BFA']
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        marker=dict(
            colors=colors[:len(labels)],
            line=dict(color='#111827', width=3)
        ),
        hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>',
        textposition='auto',
        textinfo='percent+label'
    )])
    
    fig.update_layout(
        title=dict(
            text='Resolution Type',
            font=dict(size=18, color='#F8FAFC', family='Poppins'),
            x=0.5,
            xanchor='center'
        ),
        paper_bgcolor='rgba(15, 23, 42, 0.8)',
        plot_bgcolor='rgba(15, 23, 42, 0.8)',
        font=dict(family='Inter', color='#94A3B8'),
        showlegend=True,
        legend=dict(
            orientation='v',
            yanchor='middle',
            y=0.5,
            xanchor='left',
            x=1.02,
            font=dict(color='#94A3B8')
        ),
        height=400,
        margin=dict(t=60, b=20, l=20, r=120)
    )
    
    st.plotly_chart(fig, use_container_width=True, key='chart_resolution_type')


def render_root_cause_radar(df: pd.DataFrame):
    """
    Render Root Cause Analysis radar chart.
    
    Args:
        df: Filtered DataFrame
    """
    from utils.aggregations import count_by
    
    counts = count_by(df, 'Root_Cause')
    if not counts:
        st.info("No data available for root cause analysis")
        return
    
    labels = list(counts.keys())
    values = list(counts.values())
    
    fig = go.Figure(data=[go.Scatterpolar(
        r=values,
        theta=labels,
        fill='toself',
        fillcolor='rgba(248, 113, 113, 0.18)',
        line=dict(color='#F87171', width=2),
        marker=dict(
            color='#EF4444',
            size=8,
            line=dict(color='#111827', width=2)
        ),
        hovertemplate='<b>%{theta}</b><br>Count: %{r}<extra></extra>',
        name='Root Cause Count'
    )])
    
    fig.update_layout(
        title=dict(
            text='Root Cause Analysis',
            font=dict(size=18, color='#F8FAFC', family='Poppins'),
            x=0.5,
            xanchor='center'
        ),
        paper_bgcolor='rgba(15, 23, 42, 0.8)',
        plot_bgcolor='rgba(15, 23, 42, 0.8)',
        font=dict(family='Inter', color='#94A3B8'),
        polar=dict(
            bgcolor='rgba(15, 23, 42, 0.4)',
            radialaxis=dict(
                visible=True,
                showticklabels=False,
                gridcolor='rgba(255, 255, 255, 0.06)',
                linecolor='rgba(255, 255, 255, 0.06)'
            ),
            angularaxis=dict(
                gridcolor='rgba(255, 255, 255, 0.06)',
                linecolor='rgba(255, 255, 255, 0.06)',
                color='#94A3B8'
            )
        ),
        showlegend=False,
        height=400,
        margin=dict(t=60, b=40, l=80, r=80)
    )
    
    st.plotly_chart(fig, use_container_width=True, key='chart_root_cause')
