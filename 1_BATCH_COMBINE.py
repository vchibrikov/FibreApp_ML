import os
import shutil

def combine_images(parent_folder1, parent_folder2, combined_folder):
    """
    Combines images from matching subfolders in two parent folders into a combined folder,
    omitting duplicates based on file names and sizes.
    
    Args:
    - parent_folder1 (str): Path to the first parent folder.
    - parent_folder2 (str): Path to the second parent folder.
    - combined_folder (str): Path where combined images should be saved.
    """
    # Create the combined folder if it does not exist
    os.makedirs(combined_folder, exist_ok=True)
    
    # List all subfolders in the first parent folder
    subfolders1 = [name for name in os.listdir(parent_folder1) if os.path.isdir(os.path.join(parent_folder1, name))]

    for subfolder_name in subfolders1:
        # Define paths to subfolders in both parent folders
        subfolder1_path = os.path.join(parent_folder1, subfolder_name)
        subfolder2_path = os.path.join(parent_folder2, subfolder_name)
        combined_subfolder_path = os.path.join(combined_folder, subfolder_name)

        # Create a combined subfolder if it doesn't exist
        os.makedirs(combined_subfolder_path, exist_ok=True)
        
        # Track the files already copied to avoid duplicates
        existing_files = set(os.listdir(combined_subfolder_path))
        
        # Copy images from the first subfolder
        if os.path.exists(subfolder1_path):
            for image_name in os.listdir(subfolder1_path):
                image_path = os.path.join(subfolder1_path, image_name)
                if os.path.isfile(image_path):
                    combined_image_path = os.path.join(combined_subfolder_path, image_name)
                    
                    # Check if the file is already in the combined folder
                    if image_name not in existing_files:
                        shutil.copy(image_path, combined_image_path)
                        existing_files.add(image_name)
        
        # Copy images from the second subfolder if it exists
        if os.path.exists(subfolder2_path):
            for image_name in os.listdir(subfolder2_path):
                image_path = os.path.join(subfolder2_path, image_name)
                combined_image_path = os.path.join(combined_subfolder_path, image_name)
                
                if os.path.isfile(image_path):
                    # Check if the file is already in the combined folder
                    if image_name not in existing_files:
                        shutil.copy(image_path, combined_image_path)
                        existing_files.add(image_name)

        print(f"Combined images from '{subfolder_name}' into '{combined_subfolder_path}'")

# Define the paths to the parent folders and the output folder for combined images
parent_folder1 = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG_Android/TRAIN_BATCH'
parent_folder2 = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG_Android/TEST_BATCH'
combined_folder = parent_folder1  # Use one of the parent folders as the combined output

# Run the function to combine images
combine_images(parent_folder1, parent_folder2, combined_folder)