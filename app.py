import streamlit as st
import pandas as pd
from io import StringIO

st.title("CSV File Uploader and Viewer")

# File upload option
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    try:
        # Convert the file to a string buffer
        string_data = StringIO(uploaded_file.getvalue().decode("utf-8"))
        
        # Read the CSV data into a DataFrame
        df = pd.read_csv(string_data, delimiter=';')
        
        # Display the DataFrame
        st.write("### Uploaded CSV file:")
        st.write(df)
        
    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.info("Please upload a CSV file.")
