import zipfile
import os

def extract_file(zip_file_path, target_dir):
    """
    Unzips a file to a specified directory.

    :param zip_file_path: The path to the ZIP file.
    :param extract_to_dir: The directory where files should be extracted.
    """
    # Check if the file exists
    if not os.path.isfile(zip_file_path):
        print(f"File '{zip_file_path}' not found.")
        return

    # Create the directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Open the ZIP file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # List all the files in the ZIP file
        file_list = zip_ref.namelist()
        print(f"Files in the ZIP archive: {file_list}")
        
        # Filter and extract only the CSV files
        csv_files = [file for file in file_list if file.endswith('.csv')]
        print(f"CSV files to extract: {csv_files}")
        
        for csv_file in csv_files:
            zip_ref.extract(csv_file, target_dir)
            print(f"Extracted '{csv_file}' to '{target_dir}'")

if __name__ == "__main__":
    # Example usage
    zip_file = 'C:\\Users\\ajkay\\OneDrive\\Documents\\src\\Instacart-mkt-basket.zip'
    output_dir = 'C:\\Users\\ajkay\\OneDrive\\Documents\\tgt'

    extract_file(zip_file, output_dir)
