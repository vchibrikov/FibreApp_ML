from PIL import Image
import os

input_directory = '/Users/path/to/input/directory'
output_directory = '/Users/path/to/output/directory'

size = (300, 300)

def resize_image(image_path, output_path, size):
    with Image.open(image_path) as img:
        img = img.convert('RGBA')
        
        new_img = Image.new('RGBA', size, (255, 255, 255, 0))
        
        img.thumbnail(size, Image.LANCZOS)
        paste_position = ((size[0] - img.width) // 2, (size[1] - img.height) // 2)
        new_img.paste(img, paste_position)

        file_extension = os.path.splitext(output_path)[1].lower()
        if file_extension in ['.png', '.gif', '.bmp']:
            new_img.save(output_path, format='PNG')
        else:
            rgb_img = new_img.convert('RGB')
            rgb_img.save(output_path, format='JPEG')

def process_directory(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                file_path = os.path.join(root, file)
                
                relative_path = os.path.relpath(root, input_dir)
                output_subfolder = os.path.join(output_dir, relative_path)
                os.makedirs(output_subfolder, exist_ok=True)
                
                output_path = os.path.join(output_subfolder, file)
                
                resize_image(file_path, output_path, size)

print("Processing and resizing images...")
process_directory(input_directory, output_directory)
print("Resizing complete!")
