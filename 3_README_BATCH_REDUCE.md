# BATCH_REDUCE.py
This Python script limits the number of images in each subfolder within a given directory, keeping only a specified maximum number of images. It ensures that no subfolder exceeds the defined limit by removing excess images.

- Visual Studio Code release used: 1.93.1
- Python release used: 3.12.4. 64-bit
> Warning! There are no guarantees this code will run on your machine.

## Features
- Image limiting: ensures each subfolder in the specified directory contains no more than the defined number of images.
- Batch processing: can handle multiple directories and different maximum image counts for each.
- Cross-platform compatibility: utilizes Python's os and shutil libraries for file operations, ensuring compatibility across different operating systems.

## Dependencies
The script uses the following Python libraries:

- os
- shutil

## Parameters
- directory: the path to the main directory containing subfolders with images.
- max_images: the maximum number of images to retain in each subfolder.

## Description
The script follows these steps to limit images in subfolders:

### Library Imports
The script imports necessary libraries, os for directory traversal, and shutil for file operations.
```
import os
import shutil
```

### Function to Limit Images
The limit_images_in_subfolders function ensures that each subfolder in a specified directory retains only up to max_images images, removing any excess images.
```
def limit_images_in_subfolders(directory, max_images):
    for subfolder in os.listdir(directory):
        subfolder_path = os.path.join(directory, subfolder)
        if os.path.isdir(subfolder_path):
            images = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]
            if len(images) > max_images:
                images_to_remove = images[max_images:]
                for image in images_to_remove:
                    image_path = os.path.join(subfolder_path, image)
                    os.remove(image_path)
                    print(f"Removed {image_path}")
```

### Main Function Calls
This section sets the paths for training, testing, and validation directories, and applies the limit_images_in_subfolders function to each, specifying different image limits for each set.
```
train_batch_dir = '/Users/path/to/train/batch'
test_batch_dir = '/Users/path/to/test/batch'
valid_batch_dir = '/Users/path/to/validation/batch'

limit_images_in_subfolders(train_batch_dir, 70)
limit_images_in_subfolders(test_batch_dir, 20)
limit_images_in_subfolders(valid_batch_dir, 10)

print("Image cleanup complete.")
```

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
