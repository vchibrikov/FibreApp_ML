# RAND_FILENAME_GEN.py
This Python script renames all files in a specified directory (and its subdirectories) to random UUIDs. This is particularly useful for anonymizing files or ensuring unique filenames.

- Visual Studio Code release used: 1.93.1
- Python release used: 3.12.4 (64-bit)
> Warning: There are no guarantees this code will run on your machine.

## Features
- Random filename generation: uses UUIDs to generate unique filenames, reducing the risk of naming conflicts.
- Recursive traversal: processes files in the specified directory and all of its subdirectories.

## Prerequisites
The script does not require any external libraries. It uses built-in Python modules.

## Parameters
- root_folder_path: the path to the root directory containing files that need to be renamed.

## Description
The script traverses the specified root directory and renames each file with a new name generated from a random UUID. Each new filename has a .jpeg extension.

## Key Function
### rename_files_to_random(root_folder_path)
Traverses the directory tree and renames each file found:
```
def rename_files_to_random(root_folder_path):
    for dirpath, _, filenames in os.walk(root_folder_path):
        for old_filename in filenames:
            old_file_path = os.path.join(dirpath, old_filename)
            new_filename = str(uuid.uuid4()) + '.jpeg'
            new_file_path = os.path.join(dirpath, new_filename)
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {old_filename} to {new_filename} in {dirpath}")
```
### Main Functionality
Set the path for the root directory containing files and run the renaming process:
```
if __name__ == "__main__":
    root_folder_path = '/Users/path/to/files/'
    
    rename_files_to_random(root_folder_path)
```
## License
This project is licensed under the MIT License. See the LICENSE file for more information.
