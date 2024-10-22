import os
import uuid

def rename_files_to_random(root_folder_path):
    for dirpath, _, filenames in os.walk(root_folder_path):
        for old_filename in filenames:
            old_file_path = os.path.join(dirpath, old_filename)
            new_filename = str(uuid.uuid4()) + '.jpeg'
            new_file_path = os.path.join(dirpath, new_filename)
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {old_filename} to {new_filename} in {dirpath}")

if __name__ == "__main__":
    root_folder_path = '/Users/path/to/files/'
    
    rename_files_to_random(root_folder_path)
