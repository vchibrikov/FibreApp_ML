# IMAGE_PREVALIDATION.py
This Python script validates image files in a specified directory (and its subdirectories) to ensure they are not corrupted. If a corrupted image is detected, it is automatically removed. This is particularly useful for cleaning up image datasets by removing unusable files.

- Visual Studio Code release used: 1.93.1
- Python release used: 3.12.4 (64-bit)
> Warning: There are no guarantees this code will run on your machine.

## Features
- Image validation: verifies the integrity of images using the PIL library, ensuring they are properly formatted.
- Automatic cleanup: deletes corrupted or unopenable images to maintain a clean dataset.
- Recursive traversal: processes images in the specified directory and all of its subdirectories.

## Prerequisites
The Pillow library is required. Install it using:
```
pip install pillow
```

## Parameters
- directory: The path to the root directory containing the images that need to be validated.

## Description
The script traverses the specified root directory, attempts to open and verify each image, and deletes any file that is found to be corrupted. It helps ensure that only valid images remain in the dataset.

## Key Function
### validate_images(directory)
Traverses the directory tree and validates each image:
```
def validate_images(directory):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(subdir, file)
            try:
                with Image.open(file_path) as img:
                    img.verify()
            except (UnidentifiedImageError, ValueError, Exception) as e:
                print(f"Corrupted image found and removed: {file_path}, error: {e}")
                os.remove(file_path)
```

### Main Functionality
Specify the paths of directories containing images to validate, and run the validation process:
```
    validate_images('/Users/path/to/folder/1')
    validate_images('/Users/path/to/folder/2')
    validate_images('/Users/path/to/folder/3')
```

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
