import os
from PIL import Image
import imagehash

def get_image_hash(image_path):
    with Image.open(image_path) as img:
        return imagehash.average_hash(img)

def find_and_delete_duplicates(directory):
    seen_hashes = set()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            try:
                img_hash = get_image_hash(file_path)
                if img_hash in seen_hashes:
                    print(f"Deleting duplicate image:{file_path}")
                    os.remove(file_path)
                else:
                    seen_hashes.add(img_hash)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    directory_path = "/Users/path/to/batch"
    find_and_delete_duplicates(directory_path)
