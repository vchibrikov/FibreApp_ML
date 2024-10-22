import os
import shutil

def combine_images(parent_folder1, parent_folder2, combined_folder):

    os.makedirs(combined_folder, exist_ok=True)

    subfolders1 = [name for name in os.listdir(parent_folder1) if os.path.isdir(os.path.join(parent_folder1, name))]

    for subfolder_name in subfolders1:
        # Define paths to subfolders in both parent folders
        subfolder1_path = os.path.join(parent_folder1, subfolder_name)
        subfolder2_path = os.path.join(parent_folder2, subfolder_name)
        combined_subfolder_path = os.path.join(combined_folder, subfolder_name)

        os.makedirs(combined_subfolder_path, exist_ok=True)
        
        existing_files = set(os.listdir(combined_subfolder_path))
        
        if os.path.exists(subfolder1_path):
            for image_name in os.listdir(subfolder1_path):
                image_path = os.path.join(subfolder1_path, image_name)
                if os.path.isfile(image_path):
                    combined_image_path = os.path.join(combined_subfolder_path, image_name)
                    
                    if image_name not in existing_files:
                        shutil.copy(image_path, combined_image_path)
                        existing_files.add(image_name)
        
        if os.path.exists(subfolder2_path):
            for image_name in os.listdir(subfolder2_path):
                image_path = os.path.join(subfolder2_path, image_name)
                combined_image_path = os.path.join(combined_subfolder_path, image_name)
                
                if os.path.isfile(image_path):
                    if image_name not in existing_files:
                        shutil.copy(image_path, combined_image_path)
                        existing_files.add(image_name)

        print(f"Combined images from '{subfolder_name}' into '{combined_subfolder_path}'")

parent_folder1 = '/Users/forder/with/train/data'
parent_folder2 = '/Users/folder/with/test/data'
combined_folder = parent_folder1

combine_images(parent_folder1, parent_folder2, combined_folder)
