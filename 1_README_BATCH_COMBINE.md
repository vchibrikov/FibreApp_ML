# 1_BATCH_COMBINE.py
This Python script combines images from two parent folders into a specified output folder. It merges images from corresponding subfolders in two directories (parent_folder1 and parent_folder2) into a combined directory, ensuring that no duplicate files are created during the copying process.

- Visual Studio Code release used: 1.93.1
- Python release used: 3.12.4. 64-bit
> Warning! There are no guarantees this code will run on your machine.

## Features
- Combining images: merges images from corresponding subfolders in two parent directories.
- Avoids duplicates: ensures that files with the same name are not duplicated in the combined directory.
- Automatic folder creation: creates the necessary directory structure in the output directory if it does not already exist.
- Cross-platform compatibility: uses os and shutil libraries to ensure compatibility across different operating systems.

## Dependencies
The script uses the following Python libraries:
- os
- shutil

## Parameters
- parent_folder1: path to the first parent folder containing subfolders with images.
- parent_folder2: path to the second parent folder containing subfolders with images.
- combined_folder: directory where the combined images will be saved. Subfolders will be created automatically based on the names of the subfolders in the input directories.

## Description
The script follows several key steps to achieve the image combination:

### Library Imports
The script imports the necessary libraries, os and shutil, for file and directory manipulation.
```
import os
import shutil
```

### Function to Combine Images
The combine_images function is the core of the script. It creates the output folder if it does not exist, then iterates through subfolders in parent_folder1 and parent_folder2, copying images into the specified combined_folder.
```
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
        
        if os.path.exists(subfolder1_path):
            for image_name in os.listdir(subfolder1_path):
                image_path = os.path.join(subfolder1_path, image_name)
                if os.path.isfile(image_path):
                    combined_image_path = os.path.join(combined_subfolder_path, image_name)
                    
                    if image_name not in existing_files:
                        shutil.copy(image_path, combined_image_path)
                        existing_files.add(image_name)
        
        if os.path.exists(subfolder2_path):
            for image_name in os.listdir(subfolder2_path):
                image_path = os.path.join(subfolder2_path, image_name)
                combined_image_path = os.path.join(combined_subfolder_path, image_name)
                
                if os.path.isfile(image_path):
                    if image_name not in existing_files:
                        shutil.copy(image_path, combined_image_path)
                        existing_files.add(image_name)

        print(f"Combined images from '{subfolder_name}' into '{combined_subfolder_path}'")
```

### Main Function Call
This block executes the script, defining the paths for the parent folders and the combined folder. It triggers the combine_images function to process and merge the images.
```
parent_folder1 = '/Users/folder/with/train/data'
parent_folder2 = '/Users/folder/with/test/data'
combined_folder = parent_folder1

combine_images(parent_folder1, parent_folder2, combined_folder)
```

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
