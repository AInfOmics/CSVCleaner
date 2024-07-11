# File Uploader and Viewer

This Streamlit application allows users to upload files of various types (CSV, Excel, text files, etc.) and displays their contents in a readable format.

## Features

- Upload and display CSV files as dataframes.
- Upload and display Excel files as dataframes.
- Upload and display other file types as plain text.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to access the app.

3. Upload a file using the file uploader. The app will automatically detect the file type and display its contents accordingly.

## File Types Supported

- CSV (.csv)
- Excel (.xls, .xlsx)
- Text files and other file types
- # CSVCleaner
