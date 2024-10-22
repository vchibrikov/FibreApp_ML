import os
import tensorflow as tf

train_dir = '/Users/path/to/train/batch'
test_dir = '/Users/path/to/test/batch'

img_height = 150
img_width = 150

def is_image_file(filepath):
    try:
        img = tf.io.read_file(filepath)
        img = tf.image.decode_image(img, channels=3, expand_animations=False)
        return True
    except (tf.errors.InvalidArgumentError, ValueError):
        return False

def remove_invalid_images(directory):
    for subdir, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(subdir, file)
            if not is_image_file(filepath):
                print(f"Removing invalid file: {filepath}")
                os.remove(filepath)

remove_invalid_images(train_dir)
remove_invalid_images(test_dir)

print("Image filtering complete. Invalid images removed.")
