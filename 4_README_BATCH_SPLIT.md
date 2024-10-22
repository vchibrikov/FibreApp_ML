# BATCH_SPLIT/py
This Python script splits images from subfolders of an original directory into two destination directories based on specified ratios. It helps in partitioning data into subsets, such as training, validation, and testing datasets.

- Visual Studio Code release used: 1.93.1
- Python release used: 3.12.4. 64-bit
> Warning! There are no guarantees this code will run on your machine.

## Features
Image splitting: splits images randomly from each subfolder of a specified directory into two separate subdirectories.
Customizable ratios: allows setting the proportion of images to move into each destination directory.
Data organization: keeps the structure of the subfolders intact while performing the split, ensuring data remains organized.

## Dependencies
The script uses the following Python libraries:

- os
- shutil
- random

## Parameters
- original_dir: the path to the main directory containing subfolders with images to be split.
- dest_dir1: the path to the first destination directory.
- dest_dir2: the path to the second destination directory.
- ratio1: the proportion of images to move to dest_dir1. (Default: 0.1 or 10%)
- ratio2: the proportion of images to move to dest_dir2. (Default: 0.2 or 20%)

## Description
The script follows these steps to split images:

### Library Imports
The script imports necessary libraries, os for directory traversal, shutil for file operations, and random for shuffling the images.
```
import os
import shutil
import random
```

### Function to Split Images
The split_images function moves a specified proportion of images from each subfolder of the original_dir into dest_dir1 and dest_dir2, maintaining subfolder structures.
```
def split_images(original_dir, dest_dir1, dest_dir2, ratio1 = 0.1, ratio2 = 0.2):
    os.makedirs(dest_dir1, exist_ok=True)
    os.makedirs(dest_dir2, exist_ok=True)

    for subfolder in os.listdir(original_dir):
        subfolder_path = os.path.join(original_dir, subfolder)
        if os.path.isdir(subfolder_path):
            dest_subfolder1 = os.path.join(dest_dir1, subfolder)
            dest_subfolder2 = os.path.join(dest_dir2, subfolder)
            os.makedirs(dest_subfolder1, exist_ok=True)
            os.makedirs(dest_subfolder2, exist_ok=True)

            files = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]
            random.shuffle(files)

            split_index1 = int(len(files) * ratio1)
            split_index2 = split_index1 + int(len(files) * ratio2)

            for file in files[:split_index1]:
                src_path = os.path.join(subfolder_path, file)
                dest_path = os.path.join(dest_subfolder1, file)
                shutil.move(src_path, dest_path)
                print(f"Moved {src_path} to {dest_path}")

            for file in files[split_index1:split_index2]:
                src_path = os.path.join(subfolder_path, file)
                dest_path = os.path.join(dest_subfolder2, file)
                shutil.move(src_path, dest_path)
                print(f"Moved {src_path} to {dest_path}")

    print("Image splitting complete.")
```

### Main Function Calls
Set the paths for the original directory and the two destination directories, then run the split_images function with the desired ratios.
```
original_dir = '/Users/original/directory'
destination_dir1 = '/Users/destination/directory/1'
destination_dir2 = '/Users/destination/directory/2'
```
## License
This project is licensed under the MIT License. See the LICENSE file for more information.
