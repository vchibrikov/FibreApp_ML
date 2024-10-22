# IMAGE_SQUARING.py
This Python script resizes images from a specified input directory and saves them into an output directory, maintaining aspect ratio and centering each image within a new canvas of specified dimensions. The script supports various image formats including PNG, JPEG, BMP, and GIF.

- Visual Studio Code release used: 1.93.1
- Python release used: 3.12.4 (64-bit)
> Warning: There are no guarantees this code will run on your machine.

## Features
- Resizing with aspect ratio: resizes images while preserving their aspect ratio and centers them on a new canvas of the specified size.
- Supports multiple formats: handles PNG, JPEG, BMP, and GIF files.
- Batch processing: processes images in the input directory recursively, retaining their original folder structure in the output directory.

## Prerequisites
The script requires the following Python library:
- pillow

## Parameters
- input_directory: path to the directory containing the images to resize.
- output_directory: path to the directory where the resized images will be saved.
- size: a tuple (width, height) specifying the size of the new image canvas (default: (300, 300)).

## Description
The script works by iterating through the specified input directory and processing each image file, resizing it and saving it to the corresponding location in the output directory.

### Key Functions
Resizes an image while maintaining its aspect ratio, centers it on a new canvas of the given size, and saves it in the appropriate format (PNG for transparent images, JPEG for others).
```
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
```

Processes all images within the input directory, maintaining the original folder structure in the output directory. It calls resize_image for each valid image file.
```
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
```

### Main Functionality
Set the paths for the input and output directories, then call process_directory to resize the images:
```
- input_directory = '/Users/path/to/input/directory'
- output_directory = '/Users/path/to/output/directory'

size = (300, 300)

print("Processing and resizing images...")
process_directory(input_directory, output_directory)
print("Resizing complete!")
```
## License
This project is licensed under the MIT License. See the LICENSE file for more information.
