from PIL import Image, UnidentifiedImageError
import os

def validate_images(directory):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(subdir, file)
            try:
                with Image.open(file_path) as img:
                    img.verify()  # Verify that the image is not corrupted
            except (UnidentifiedImageError, ValueError, Exception) as e:
                print(f"Corrupted image found and removed: {file_path}, error: {e}")
                os.remove(file_path)  # Remove the corrupted image

# Run validation on your dataset directories
validate_images('/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG/TRAIN_BATCH')
validate_images('/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG/TEST_BATCH')
