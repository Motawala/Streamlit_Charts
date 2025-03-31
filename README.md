# Interactive Data Visualization App

A Streamlit application that allows users to upload their data and create various types of interactive charts.

## Features

- Upload CSV or Excel files
- Create multiple types of charts:
  - Line Charts
  - Bar Charts
  - Scatter Plots
  - Pie Charts
  - Box Plots
  - Histograms
- Customize chart appearance:
  - Chart title
  - Axis labels
  - Legend visibility
  - Color schemes
- Interactive data preview
- Responsive layout

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Upload your CSV or Excel file using the file uploader
2. Preview your data in the data preview section
3. Select the type of chart you want to create
4. Configure the chart by selecting:
   - X-axis and Y-axis columns
   - Color column (optional)
   - Chart title and labels
5. Click "Generate Chart" to create your visualization

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- Plotly
- Openpyxl (for Excel file support)
- NumPy

## File Structure

- `app.py`: Main Streamlit application
- `utils.py`: Utility functions for data processing
- `charts.py`: Chart creation functions
- `requirements.txt`: Project dependencies
- `README.md`: Documentation