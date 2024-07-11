import streamlit as st
import pandas as pd
from io import StringIO
import csv

st.title("CSV File Uploader and Viewer")

# File upload option
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    try:
        # Convert the file to a string buffer
        string_data = StringIO(uploaded_file.getvalue().decode("utf-8"))
        
        # Function to detect delimiter
        def detect_delimiter(data):
            try:
                sniffer = csv.Sniffer()
                sample = data.read(1024)
                data.seek(0)
                dialect = sniffer.sniff(sample)
                return dialect.delimiter
            except:
                return None
        
        # Detect the delimiter
        delimiter = detect_delimiter(string_data)
        
        if delimiter is None:
            # Fallback to common delimiters if the sniffer fails
            common_delimiters = [',', ';', '\t', '|']
            for delim in common_delimiters:
                string_data.seek(0)
                try:
                    df = pd.read_csv(string_data, delimiter=delim)
                    st.write(f"### Uploaded CSV file (detected delimiter: '{delim}'):")
                    st.write(df)
                    break
                except:
                    continue
        else:
            # Read the CSV data into a DataFrame with detected delimiter
            string_data.seek(0)
            df = pd.read_csv(string_data, delimiter=delimiter)
            st.write(f"### Uploaded CSV file (detected delimiter: '{delimiter}'):")
            st.write(df)
        
    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.info("Please upload a CSV file.")
