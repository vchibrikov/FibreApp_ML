import os
import random

def equalize_images_in_subfolders(base_dir):
    """
    Equalizes the number of images in each subfolder of the base directory.
    Ensures all subfolders have the same number of images as the subfolder with the fewest images.
    
    Parameters:
    base_dir (str): Path to the main directory containing subfolders with images.
    """
    # Store the number of images in each subfolder
    subfolder_image_counts = {}

    # Get a list of subfolders
    subfolders = [subfolder for subfolder in os.listdir(base_dir) 
                  if os.path.isdir(os.path.join(base_dir, subfolder))]

    # Get the number of images in each subfolder
    for subfolder in subfolders:
        subfolder_path = os.path.join(base_dir, subfolder)
        images = [img for img in os.listdir(subfolder_path) 
                  if os.path.isfile(os.path.join(subfolder_path, img))]
        subfolder_image_counts[subfolder] = len(images)

    # Find the minimum image count
    min_image_count = min(subfolder_image_counts.values())
    print(f"The smallest subfolder has {min_image_count} images. Adjusting all subfolders to this count.")

    # Equalize each subfolder's image count
    for subfolder in subfolders:
        subfolder_path = os.path.join(base_dir, subfolder)
        images = [img for img in os.listdir(subfolder_path) 
                  if os.path.isfile(os.path.join(subfolder_path, img))]
        
        # Randomly select images to remove if there are more than the minimum count
        if len(images) > min_image_count:
            images_to_remove = random.sample(images, len(images) - min_image_count)
            for img in images_to_remove:
                img_path = os.path.join(subfolder_path, img)
                os.remove(img_path)
                print(f"Removed {img_path}")

    print("Equalization complete.")

# Example usage:
base_dir = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG_Android_equalized/VALIDATION_BATCH'
equalize_images_in_subfolders(base_dir)