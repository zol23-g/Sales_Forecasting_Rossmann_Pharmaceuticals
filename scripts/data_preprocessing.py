import pandas as pd
import logging
def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        logging.info('Datasets loaded successfully.')
        return df
    except Exception as e:
        logging.info(f"Error loading data: {e}")
        return None

