from PIL import Image
import os

# Directory containing images
input_directory = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/MODEL_CHECK/'
output_directory = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/MODEL_CHECK_RESIZED'

# Desired size
size = (300, 300)

def resize_image(image_path, output_path, size):
    with Image.open(image_path) as img:
        # Convert image to RGBA to handle transparency
        img = img.convert('RGBA')
        
        # Create a new image with the desired size and a white background
        new_img = Image.new('RGBA', size, (255, 255, 255, 0))
        
        # Calculate the position to paste the resized image
        img.thumbnail(size, Image.LANCZOS)
        paste_position = ((size[0] - img.width) // 2, (size[1] - img.height) // 2)
        new_img.paste(img, paste_position)

        # Determine the file format based on the output path extension
        file_extension = os.path.splitext(output_path)[1].lower()
        if file_extension in ['.png', '.gif', '.bmp']:
            # Save as PNG if format supports transparency
            new_img.save(output_path, format='PNG')
        else:
            # Convert to RGB before saving as JPEG
            rgb_img = new_img.convert('RGB')
            rgb_img.save(output_path, format='JPEG')

def process_directory(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                file_path = os.path.join(root, file)
                
                # Create corresponding subfolder structure in the output directory
                relative_path = os.path.relpath(root, input_dir)
                output_subfolder = os.path.join(output_dir, relative_path)
                os.makedirs(output_subfolder, exist_ok=True)
                
                output_path = os.path.join(output_subfolder, file)
                
                # Resize the image and save it
                resize_image(file_path, output_path, size)

print("Processing and resizing images...")
process_directory(input_directory, output_directory)
print("Resizing complete!")