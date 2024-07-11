import streamlit as st
import pandas as pd
from io import StringIO

st.title("File Uploader and Viewer")

# File upload option
uploaded_file = st.file_uploader("Choose a file", type=None)

if uploaded_file is not None:
    # Read the uploaded file
    try:
        # Check the file type based on the extension
        file_extension = uploaded_file.name.split('.')[-1]

        # Different processing based on file type
        if file_extension.lower() == 'csv':
            # Convert the file to a string buffer
            string_data = StringIO(uploaded_file.getvalue().decode("utf-8"))
        
            # Read the CSV data into a DataFrame
            df = pd.read_csv(string_data, delimiter=';')
        
            # Display the DataFrame
            st.write("### Uploaded CSV file:")
            st.dataframe(df)  # Display as DataFrame
        
        elif file_extension.lower() in ['xls', 'xlsx']:
            # Read Excel file into DataFrame
            df = pd.read_excel(uploaded_file)
            st.write("### Uploaded Excel file:")
            st.dataframe(df)  # Display as DataFrame
        
        else:
            # Read as plain text for other file types
            text_data = uploaded_file.getvalue().decode("utf-8")
            # Normalize line endings
            normalized_text = text_data.replace("\r\n", "\n").replace("\r", "\n")
            st.write(f"### Uploaded {file_extension.upper()} file:")
            st.text(normalized_text)  # Display as plain text with normalized line endings
        
    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.info("Please upload a file.")
