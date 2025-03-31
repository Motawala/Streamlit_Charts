import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_line_chart(df, x_col, y_col, title, color_col=None):
    """
    Create a line chart
    """
    fig = px.line(df, x=x_col, y=y_col, color=color_col, title=title)
    return fig

def create_bar_chart(df, x_col, y_col, title, color_col=None):
    """
    Create a bar chart
    """
    fig = px.bar(df, x=x_col, y=y_col, color=color_col, title=title)
    return fig

def create_scatter_chart(df, x_col, y_col, title, color_col=None):
    """
    Create a scatter plot
    """
    fig = px.scatter(df, x=x_col, y=y_col, color=color_col, title=title)
    return fig

def create_pie_chart(df, names_col, values_col, title):
    """
    Create a pie chart
    """
    fig = px.pie(df, names=names_col, values=values_col, title=title)
    return fig

def create_box_chart(df, x_col, y_col, title, color_col=None):
    """
    Create a box plot
    """
    fig = px.box(df, x=x_col, y=y_col, color=color_col, title=title)
    return fig

def create_histogram(df, x_col, title, color_col=None):
    """
    Create a histogram
    """
    fig = px.histogram(df, x=x_col, color=color_col, title=title)
    return fig

def update_chart_layout(fig, title, x_label, y_label, show_legend=True):
    """
    Update chart layout with common settings
    """
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        showlegend=show_legend,
        template="plotly_white",
        height=600
    )
    return fig