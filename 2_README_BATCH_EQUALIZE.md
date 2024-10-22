# 2_BATCH_EQUALIZE.py
This Python script equalizes the number of images across subfolders within a specified base directory. It adjusts all subfolders to have the same number of images by reducing the count to match the smallest subfolder, randomly removing excess images.

- Visual Studio Code release used: 1.93.1
- Python release used: 3.12.4. 64-bit
> Warning! There are no guarantees this code will run on your machine.

## Features
Equalizes image count: ensures that all subfolders in the specified directory have the same number of images.
Random removal: randomly removes images from subfolders with excess images to match the count of the smallest subfolder.
Cross-platform compatibility: Uses os and random libraries to ensure compatibility across different operating systems.

## Dependencies
The script uses the following Python libraries:

- os
- random

## Parameters
base_dir: The path to the base directory containing subfolders with images to be equalized.

## Description
The script follows several key steps to equalize the images:

### Library Imports
The script imports the necessary libraries, os for file and directory handling, and random for randomly selecting images for removal.

```
import os
import random
```

### Function to Equalize Images
The equalize_images_in_subfolders function identifies the number of images in each subfolder, determines the smallest count, and then reduces the image count in other subfolders to match this minimum.
```
def equalize_images_in_subfolders(base_dir):
    subfolder_image_counts = {}
    subfolders = [subfolder for subfolder in os.listdir(base_dir) 
                  if os.path.isdir(os.path.join(base_dir, subfolder))]

    for subfolder in subfolders:
        subfolder_path = os.path.join(base_dir, subfolder)
        images = [img for img in os.listdir(subfolder_path) 
                  if os.path.isfile(os.path.join(subfolder_path, img))]
        subfolder_image_counts[subfolder] = len(images)

    min_image_count = min(subfolder_image_counts.values())
    print(f"The smallest subfolder has {min_image_count} images. Adjusting all subfolders to this count.")

    for subfolder in subfolders:
        subfolder_path = os.path.join(base_dir, subfolder)
        images = [img for img in os.listdir(subfolder_path) 
                  if os.path.isfile(os.path.join(subfolder_path, img))]
        
        if len(images) > min_image_count:
            images_to_remove = random.sample(images, len(images) - min_image_count)
            for img in images_to_remove:
                img_path = os.path.join(subfolder_path, img)
                os.remove(img_path)
                print(f"Removed {img_path}")

    print("Equalization complete.")
```

### Main Function Call
This block executes the script, setting the base_dir path and calling the equalize_images_in_subfolders function to perform the equalization.
```
base_dir = '/Users/path/to/equalization/images'
equalize_images_in_subfolders(base_dir)
```

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
