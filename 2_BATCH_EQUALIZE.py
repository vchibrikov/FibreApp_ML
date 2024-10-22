import os
import random

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

base_dir = '/Users/path/to/equalization/images'
equalize_images_in_subfolders(base_dir)
