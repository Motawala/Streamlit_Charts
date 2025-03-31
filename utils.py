import pandas as pd
import streamlit as st

def load_data(file):
    """
    Load data from CSV or Excel file
    """
    try:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file)
        else:
            st.error("Please upload a CSV or Excel file")
            return None
        return df
    except Exception as e:
        st.error(f"Error loading file: {str(e)}")
        return None

def get_numeric_columns(df):
    """
    Get list of numeric columns from dataframe
    """
    return df.select_dtypes(include=['int64', 'float64']).columns.tolist()

def get_categorical_columns(df):
    """
    Get list of categorical columns from dataframe
    """
    return df.select_dtypes(include=['object', 'category']).columns.tolist()

def validate_data(df, x_col, y_col):
    """
    Validate selected columns for chart creation
    """
    if not x_col or not y_col:
        st.error("Please select both X and Y columns")
        return False
    if x_col not in df.columns or y_col not in df.columns:
        st.error("Selected columns not found in dataset")
        return False
    return True