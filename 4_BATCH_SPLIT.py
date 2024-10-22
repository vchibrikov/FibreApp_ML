import os
import shutil
import random

def split_images(original_dir, dest_dir1, dest_dir2, ratio1 = 0.1, ratio2 = 0.2):

    os.makedirs(dest_dir1, exist_ok=True)
    os.makedirs(dest_dir2, exist_ok=True)

    for subfolder in os.listdir(original_dir):
        subfolder_path = os.path.join(original_dir, subfolder)
        if os.path.isdir(subfolder_path):
            dest_subfolder1 = os.path.join(dest_dir1, subfolder)
            dest_subfolder2 = os.path.join(dest_dir2, subfolder)
            os.makedirs(dest_subfolder1, exist_ok=True)
            os.makedirs(dest_subfolder2, exist_ok=True)

            files = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]
            random.shuffle(files)  # Shuffle the list to ensure random splitting

            split_index1 = int(len(files) * ratio1)
            split_index2 = split_index1 + int(len(files) * ratio2)

            for file in files[:split_index1]:
                src_path = os.path.join(subfolder_path, file)
                dest_path = os.path.join(dest_subfolder1, file)
                shutil.move(src_path, dest_path)
                print(f"Moved {src_path} to {dest_path}")

            for file in files[split_index1:split_index2]:
                src_path = os.path.join(subfolder_path, file)
                dest_path = os.path.join(dest_subfolder2, file)
                shutil.move(src_path, dest_path)
                print(f"Moved {src_path} to {dest_path}")

    print("Image splitting complete.")

original_dir = '/Users/original/directory'
destination_dir1 = '/Users/destination/directory/1'
destination_dir2 = '/Users/destination/directory/2'

# Split images with 20% moving to destination_dir1 and 30% moving to destination_dir2
split_images(original_dir, destination_dir1, destination_dir2, ratio1 = 0.1, ratio2 = 0.2)
