# IMG_DUPLICATE_HANDLER.py
This Python script identifies and deletes duplicate images from a specified directory using perceptual image hashing. It leverages the PIL (Pillow) library for image handling and imagehash for generating image hashes.

- Visual Studio Code release used: 1.93.1
- Python release used: 3.12.4 (64-bit)
> Warning: There are no guarantees this code will run on your machine.

## Features
- Duplicate detection: uses perceptual hashing to detect duplicate images based on their visual content, rather than filename or metadata.
- Automatic cleanup: deletes duplicate images automatically, ensuring only unique images remain in the specified directory.

## Prerequisites
The script requires the following Python libraries:
- pillow
- imagehash
 
## Parameters
directory_path: The path to the directory containing images where duplicates will be found and deleted.

## Description
The script processes each image file in the specified directory, generates a perceptual hash for each image, and checks if the hash has already been seen. If it has, the script deletes the duplicate image; otherwise, it adds the hash to the set of seen hashes.

## Key Functions
### get_image_hash(image_path)
Generates a perceptual hash for a given image file using the average hash method.
```
def get_image_hash(image_path):
    with Image.open(image_path) as img:
        return imagehash.average_hash(img)
```
### find_and_delete_duplicates(directory)
```
def find_and_delete_duplicates(directory):
    seen_hashes = set()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            try:
                img_hash = get_image_hash(file_path)
                if img_hash in seen_hashes:
                    print(f"Deleting duplicate image: {file_path}")
                    os.remove(file_path)
                else:
                    seen_hashes.add(img_hash)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
```
### Main Functionality
Set the path for the directory containing images and run the duplicate detection and deletion process:
```
if __name__ == "__main__":
    directory_path = "/Users/path/to/batch"
    find_and_delete_duplicates(directory_path)
```
## License
This project is licensed under the MIT License. See the LICENSE file for more information.
