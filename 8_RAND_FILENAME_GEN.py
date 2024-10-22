import os
import uuid

def rename_files_to_random(root_folder_path):
    # Walk through the root folder
    for dirpath, _, filenames in os.walk(root_folder_path):
        for old_filename in filenames:
            old_file_path = os.path.join(dirpath, old_filename)
            # Generate a unique random filename
            new_filename = str(uuid.uuid4()) + '.jpeg'
            new_file_path = os.path.join(dirpath, new_filename)
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {old_filename} to {new_filename} in {dirpath}")

if __name__ == "__main__":
    # Replace with the path to your root folder
    root_folder_path = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/MODEL_CHECK/'
    
    rename_files_to_random(root_folder_path)
