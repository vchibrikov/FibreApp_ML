1_BATCH_COMBINE.py
This Python script combines images from two parent folders into a specified output folder. It merges images from corresponding subfolders in two directories (parent_folder1 and parent_folder2) into a combined directory, ensuring that no duplicate files are created during the copying process.

Visual Studio Code release used: 1.93.1
Python release used: 3.12.4. 64-bit
Warning! There are no guarantees this code will run on your machine.

Features
Combining Images: Merges images from corresponding subfolders in two parent directories.
Avoids Duplicates: Ensures that files with the same name are not duplicated in the combined directory.
Automatic Folder Creation: Creates the necessary directory structure in the output directory if it does not already exist.
Cross-platform Compatibility: Uses os and shutil libraries to ensure compatibility across different operating systems.
Dependencies
The script uses the following Python libraries:

os (standard library)
shutil (standard library)
No additional installations are required as the dependencies are included in Python's standard library.

Parameters
parent_folder1: Path to the first parent folder containing subfolders with images.
parent_folder2: Path to the second parent folder containing subfolders with images.
combined_folder: Directory where the combined images will be saved. Subfolders will be created automatically based on the names of the subfolders in the input directories.
Description
The script follows several key steps to achieve the image combination:

Library Imports
The script imports the necessary libraries, os and shutil, for file and directory manipulation.

python
Копировать код
import os
import shutil
Function to Combine Images
The combine_images function is the core of the script. It creates the output folder if it does not exist, then iterates through subfolders in parent_folder1 and parent_folder2, copying images into the specified combined_folder.

python
Копировать код
def combine_images(parent_folder1, parent_folder2, combined_folder):
    os.makedirs(combined_folder, exist_ok=True)
    subfolders1 = [name for name in os.listdir(parent_folder1) if os.path.isdir(os.path.join(parent_folder1, name))]
    
    for subfolder_name in subfolders1:
        # Define paths to subfolders in both parent folders
        subfolder1_path = os.path.join(parent_folder1, subfolder_name)
        subfolder2_path = os.path.join(parent_folder2, subfolder_name)
        combined_subfolder_path = os.path.join(combined_folder, subfolder_name)

        os.makedirs(combined_subfolder_path, exist_ok=True)
        
        existing_files = set(os.listdir(combined_subfolder_path))
        
        # Copy images from subfolder1 and subfolder2 to the combined folder
        if os.path.exists(subfolder1_path):
            # Copy images from the first parent folder
            ...
        
        if os.path.exists(subfolder2_path):
            # Copy images from the second parent folder
            ...
Main Function Call
This block executes the script, defining the paths for the parent folders and the combined folder. It triggers the combine_images function to process and merge the images.

python
Копировать код
parent_folder1 = '/Users/folder/with/train/data'
parent_folder2 = '/Users/folder/with/test/data'
combined_folder = parent_folder1

combine_images(parent_folder1, parent_folder2, combined_folder)
Usage Example
Set the paths to parent_folder1, parent_folder2, and combined_folder in the script.
Run the script using a Python environment:
bash
Копировать код
python combine_images.py
The script will create subfolders in the combined_folder and merge images from corresponding subfolders in parent_folder1 and parent_folder2 without duplicating files.
License
This project is licensed under the MIT License. See the LICENSE file for more information.
