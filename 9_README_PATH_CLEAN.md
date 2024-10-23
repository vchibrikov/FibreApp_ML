# PATH_CLEAN.py
This Python script deletes all files in a specified directory (and its subdirectories). It is particularly useful for clearing out directories without deleting the directories themselves.

- Visual Studio Code release used: 1.93.1
- Python release used: 3.12.4 (64-bit)
> Warning: There are no guarantees this code will run on your machine.

## Features
- File deletion: removes all files from the specified directory and its subdirectories, while preserving the directory structure.
- Recursive traversal: processes files in the specified directory and all of its subdirectories.

## Prerequisites
The script does not require any external libraries. It uses built-in Python modules.

## Parameters
- directory_path: the path to the root directory containing files that need to be deleted.

## Description
The script traverses the specified root directory and deletes each file it finds. It does not delete any directories—only the files within them.

## Key function
### delete_files_in_directory(directory_path)
Traverses the directory tree and deletes each file found:
```
def delete_files_in_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
```

### Main Functionality
Set the path for the root directory containing files and run the deletion process:
```
if __name__ == "__main__":
    directory_path = '/Users/path/to/directory'
    
    delete_files_in_directory(directory_path)
```

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
