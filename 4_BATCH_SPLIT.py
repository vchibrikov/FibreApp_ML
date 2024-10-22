#### iOS ####
# import os
# import shutil
# import random

# def split_images(original_dir, destination_dir, split_ratio = 0.2):
#     """
#     Split images in each subfolder of the original_dir into two groups:
#     1. Move 'split_ratio' of the images to destination_dir, while keeping the original structure.
#     2. Leave the rest in the original_dir.
#     """
#     # Ensure destination_dir exists
#     if not os.path.exists(destination_dir):
#         os.makedirs(destination_dir)

#     for subfolder in os.listdir(original_dir):
#         subfolder_path = os.path.join(original_dir, subfolder)
#         if os.path.isdir(subfolder_path):
#             # Create corresponding subfolder in the destination directory
#             destination_subfolder = os.path.join(destination_dir, subfolder)
#             if not os.path.exists(destination_subfolder):
#                 os.makedirs(destination_subfolder)

#             # List all files in the current subfolder
#             files = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]
#             random.shuffle(files)  # Shuffle the list to ensure random splitting

#             # Calculate the split point
#             split_index = int(len(files) * split_ratio)

#             # Move the files to the destination subfolder
#             for file in files[:split_index]:
#                 src_path = os.path.join(subfolder_path, file)
#                 dest_path = os.path.join(destination_subfolder, file)
#                 shutil.move(src_path, dest_path)
#                 print(f"Moved {src_path} to {dest_path}")

# # Define paths to the directories
# original_dir = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG_iOS/TRAIN_BATCH'
# destination_dir = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG_iOS/TEST_BATCH'

# # Split images with 20% moving to destination_dir
# split_images(original_dir, destination_dir, split_ratio = 0.2)

# print("Image splitting complete.")





#### Android ####
import os
import shutil
import random

def split_images(original_dir, dest_dir1, dest_dir2, ratio1 = 0.1, ratio2 = 0.2):
    """
    Split images in each subfolder of the original_dir into three groups:
    1. Move 'ratio1' of the images to dest_dir1.
    2. Move 'ratio2' of the images to dest_dir2.
    3. Leave the remaining images in the original_dir.
    
    Args:
    - original_dir (str): Path to the original directory containing subfolders of images.
    - dest_dir1 (str): Path to the first destination directory.
    - dest_dir2 (str): Path to the second destination directory.
    - ratio1 (float): The fraction of images to move to dest_dir1 (e.g., 0.2 means 20%).
    - ratio2 (float): The fraction of images to move to dest_dir2 (e.g., 0.3 means 30%).
    """
    # Ensure destination directories exist
    os.makedirs(dest_dir1, exist_ok=True)
    os.makedirs(dest_dir2, exist_ok=True)

    for subfolder in os.listdir(original_dir):
        subfolder_path = os.path.join(original_dir, subfolder)
        if os.path.isdir(subfolder_path):
            # Create corresponding subfolders in both destination directories
            dest_subfolder1 = os.path.join(dest_dir1, subfolder)
            dest_subfolder2 = os.path.join(dest_dir2, subfolder)
            os.makedirs(dest_subfolder1, exist_ok=True)
            os.makedirs(dest_subfolder2, exist_ok=True)

            # List all files in the current subfolder
            files = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]
            random.shuffle(files)  # Shuffle the list to ensure random splitting

            # Calculate split points
            split_index1 = int(len(files) * ratio1)
            split_index2 = split_index1 + int(len(files) * ratio2)

            # Move the files to the first destination subfolder
            for file in files[:split_index1]:
                src_path = os.path.join(subfolder_path, file)
                dest_path = os.path.join(dest_subfolder1, file)
                shutil.move(src_path, dest_path)
                print(f"Moved {src_path} to {dest_path}")

            # Move the files to the second destination subfolder
            for file in files[split_index1:split_index2]:
                src_path = os.path.join(subfolder_path, file)
                dest_path = os.path.join(dest_subfolder2, file)
                shutil.move(src_path, dest_path)
                print(f"Moved {src_path} to {dest_path}")

    print("Image splitting complete.")

# Define paths to the directories
original_dir = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG_Android/TRAIN_BATCH'
destination_dir1 = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG_Android/VALIDATION_BATCH'
destination_dir2 = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG_Android/TEST_BATCH'

# Split images with 20% moving to destination_dir1 and 30% moving to destination_dir2
split_images(original_dir, destination_dir1, destination_dir2, ratio1 = 0.1, ratio2 = 0.2)
