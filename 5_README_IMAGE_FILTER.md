# 5_IMAGE_FILTER.py
This Python script filters out invalid image files from specified directories. It uses TensorFlow to check if files are valid images and removes those that cannot be properly decoded. This is particularly useful for cleaning datasets before training a machine learning model.

- Visual Studio Code release used: 1.93.1
- Python release used: 3.12.4. 64-bit
> Warning! There are no guarantees this code will run on your machine.

## Features
- Invalid Image Detection: Uses TensorFlow to detect and remove files that are not valid images.
- Batch Processing: Processes all subdirectories within a specified directory, ensuring that each image is checked.
- Error Handling: Safely handles decoding errors to avoid crashes during dataset preparation.

## Dependencies
The script requires the following Python libraries:

- os (standard library)
- tensorflow (install via pip):

## Parameters
train_dir: Path to the directory containing training images.
test_dir: Path to the directory containing test images.
img_height: Height to resize images for validation (default: 150).
img_width: Width to resize images for validation (default: 150).

## Description
The script follows these steps to filter invalid images:

### Library imports
The script imports the necessary libraries, os for file handling and tensorflow for image validation.
```
import os
import tensorflow as tf
```

### Function to check image validity
The is_image_file function attempts to read and decode an image file using TensorFlow. If the file is invalid, an exception is caught, and the function returns False.
```
def is_image_file(filepath):
    try:
        img = tf.io.read_file(filepath)
        img = tf.image.decode_image(img, channels=3, expand_animations=False)
        return True
    except (tf.errors.InvalidArgumentError, ValueError):
        return False
```

### Function to remove invalid images
The remove_invalid_images function iterates through all files in the specified directory and its subdirectories, removing files that are not valid images.
```
def remove_invalid_images(directory):
    for subdir, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(subdir, file)
            if not is_image_file(filepath):
                print(f"Removing invalid file: {filepath}")
                os.remove(filepath)
```

### Main function calls
Specify the paths to your directories containing training and testing images, then call the remove_invalid_images function for each directory.
```
train_dir = '/Users/path/to/train/batch'
test_dir = '/Users/path/to/test/batch'

remove_invalid_images(train_dir)
remove_invalid_images(test_dir)

print("Image filtering complete. Invalid images removed.")
```

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
