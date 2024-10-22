import os
import tensorflow as tf

# Define paths to directories
train_dir = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG/TRAIN_BATCH'
test_dir = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG/TEST_BATCH'

# Parameters
img_height = 150
img_width = 150

# Function to check if a file is a valid image
def is_image_file(filepath):
    try:
        img = tf.io.read_file(filepath)
        img = tf.image.decode_image(img, channels=3, expand_animations=False)
        return True
    except (tf.errors.InvalidArgumentError, ValueError):
        return False

# Function to remove invalid images
def remove_invalid_images(directory):
    for subdir, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(subdir, file)
            if not is_image_file(filepath):
                print(f"Removing invalid file: {filepath}")
                os.remove(filepath)

# Remove invalid images from both directories
remove_invalid_images(train_dir)
remove_invalid_images(test_dir)

print("Image filtering complete. Invalid images removed.")
