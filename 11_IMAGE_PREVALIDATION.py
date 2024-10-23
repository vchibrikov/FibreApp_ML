from PIL import Image, UnidentifiedImageError
import os

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

validate_images('/Users/path/to/folder/1')
validate_images('/Users/path/to/folder/2')
validate_images('/Users/path/to/folder/3')
