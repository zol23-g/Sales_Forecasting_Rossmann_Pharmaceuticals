import unittest
import pandas as pd
from scripts.data_preprocessing import load_data

class TestLoadData(unittest.TestCase):
    
    def test_load_data(self):
        # Create a sample DataFrame
        data = {
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9]
        }
        expected_df = pd.DataFrame(data)
        
        # Save the sample DataFrame to a CSV file
        test_file_path = 'test_data.csv'
        expected_df.to_csv(test_file_path, index=False)
        
        # Load the data using the load_data function
        result_df = load_data(test_file_path)
        
        # Check if the loaded DataFrame matches the expected DataFrame
        pd.testing.assert_frame_equal(result_df, expected_df)

if __name__ == '__main__':
    unittest.main()
