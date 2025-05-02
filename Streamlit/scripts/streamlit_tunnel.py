import streamlit as st
import os
import threading
import subprocess  # Import subprocess for better process management
import time
import logging

def run_streamlit():
    """Function to run the Streamlit app."""
    try:
        # Use subprocess.Popen for better control
        process = subprocess.Popen(
            ["streamlit", "run", "base_app.py", "--logger.level=debug"],
            stdout=subprocess.PIPE,  # Capture stdout
            stderr=subprocess.PIPE,  # Capture stderr
        )

        # Monitor process for errors and output
        while True:
            output = process.stdout.readline()
            error = process.stderr.readline()

            if output:
                logging.info(output.decode().strip())
            if error:
                logging.error(error.decode().strip())

            if process.poll() is not None:  # Check if process has ended
                break

            time.sleep(0.1)  # Adjust sleep interval if needed

    except Exception as e:
        logging.exception(f"An error occurred while running Streamlit: {e}")

# Configure logging (optional)
logging.basicConfig(
    level=logging.INFO,  # Set to DEBUG for more detailed logs
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# Start Streamlit in a separate thread
streamlit_thread = threading.Thread(target=run_streamlit)
streamlit_thread.start()