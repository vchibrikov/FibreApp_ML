import os
import shutil

def limit_images_in_subfolders(directory, max_images):
    """
    Keep only 'max_images' images in each subfolder of the given directory.
    """
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

# Define paths to the directories
train_batch_dir = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG_Android_clean/TRAIN_BATCH'
test_batch_dir = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG_Android_clean/TEST_BATCH'
valid_batch_dir = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG_Android_clean/VALIDATION_BATCH'

limit_images_in_subfolders(train_batch_dir, 100)
limit_images_in_subfolders(test_batch_dir, 20)
limit_images_in_subfolders(valid_batch_dir, 10)


print("Image cleanup complete.")
