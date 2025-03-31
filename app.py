import streamlit as st
import pandas as pd
from utils import load_data, get_numeric_columns, get_categorical_columns, validate_data
from charts import (
    create_line_chart, create_bar_chart, create_scatter_chart,
    create_pie_chart, create_box_chart, create_histogram,
    update_chart_layout
)

# Set page config
st.set_page_config(
    page_title="Data Visualization App",
    page_icon="📊",
    layout="wide"
)

# Title and description
st.title("📊 Interactive Data Visualization")
st.markdown("""
This application allows you to upload your data and create various types of charts.
Upload a CSV or Excel file to get started!
""")

# File upload
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=['csv', 'xlsx', 'xls'])

if uploaded_file is not None:
    # Load data
    df = load_data(uploaded_file)

    if df is not None:
        # Display data preview with row selection
        st.subheader("Data Preview")
        preview_rows = st.slider("Number of rows to display", min_value=1, max_value=len(df), value=5)
        st.dataframe(df.head(preview_rows))

        # Display data info
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"Total rows: {len(df)}")
        with col2:
            st.write(f"Total columns: {len(df.columns)}")

        # Get column types
        numeric_cols = get_numeric_columns(df)
        categorical_cols = get_categorical_columns(df)

        # Chart type selection
        chart_type = st.selectbox(
            "Select Chart Type",
            ["Line Chart", "Bar Chart", "Scatter Plot", "Pie Chart", "Box Plot", "Histogram"]
        )

        # Chart configuration
        st.subheader("Chart Configuration")

        if chart_type in ["Line Chart", "Bar Chart", "Scatter Plot", "Box Plot"]:
            col1, col2 = st.columns(2)
            with col1:
                x_col = st.selectbox("Select X-axis", df.columns)
            with col2:
                y_col = st.selectbox("Select Y-axis", df.columns)
                if y_col in categorical_cols and chart_type in ["Line Chart", "Scatter Plot"]:
                    st.warning("⚠️ Selected Y-axis column is categorical. This might not be suitable for this chart type.")

            color_col = st.selectbox("Select Color Column (Optional)", [None] + categorical_cols)

        elif chart_type == "Pie Chart":
            col1, col2 = st.columns(2)
            with col1:
                names_col = st.selectbox("Select Names Column", categorical_cols)
            with col2:
                values_col = st.selectbox("Select Values Column", numeric_cols)
            color_col = None

        elif chart_type == "Histogram":
            x_col = st.selectbox("Select Column", df.columns)
            if x_col in categorical_cols:
                st.warning("⚠️ Selected column is categorical. This might not be suitable for a histogram.")
            color_col = st.selectbox("Select Color Column (Optional)", [None] + categorical_cols)
            y_col = None

        # Chart customization
        st.subheader("Chart Customization")
        title = st.text_input("Chart Title", "My Chart")
        x_label = st.text_input("X-axis Label", "")
        y_label = st.text_input("Y-axis Label", "")
        show_legend = st.checkbox("Show Legend", True)

        # Create chart
        if st.button("Generate Chart"):
            if chart_type in ["Line Chart", "Bar Chart", "Scatter Plot", "Box Plot"]:
                if validate_data(df, x_col, y_col):
                    if chart_type == "Line Chart":
                        fig = create_line_chart(df, x_col, y_col, title, color_col)
                    elif chart_type == "Bar Chart":
                        fig = create_bar_chart(df, x_col, y_col, title, color_col)
                    elif chart_type == "Scatter Plot":
                        fig = create_scatter_chart(df, x_col, y_col, title, color_col)
                    else:
                        fig = create_box_chart(df, x_col, y_col, title, color_col)

                    fig = update_chart_layout(fig, title, x_label, y_label, show_legend)
                    st.plotly_chart(fig, use_container_width=True)

            elif chart_type == "Pie Chart":
                if names_col and values_col:
                    fig = create_pie_chart(df, names_col, values_col, title)
                    fig = update_chart_layout(fig, title, "", "", show_legend)
                    st.plotly_chart(fig, use_container_width=True)

            elif chart_type == "Histogram":
                if x_col:
                    fig = create_histogram(df, x_col, title, color_col)
                    fig = update_chart_layout(fig, title, x_label, "Count", show_legend)
                    st.plotly_chart(fig, use_container_width=True)