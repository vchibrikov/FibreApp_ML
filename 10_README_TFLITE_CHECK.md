# TFLITE_CHECK.py
This Python script processes images in a specified directory using a TFLite model, classifies them, and renames each image file based on the predicted class. It is particularly useful for categorizing and organizing images by appending class labels to their filenames.

- Visual Studio Code release used: 1.93.1
- Python release used: 3.12.4 (64-bit)
> Warning: There are no guarantees this code will run on your machine.

## Features
- Image classification: uses a TensorFlow Lite model to classify images.
- Batch image processing: processes all images in the specified folder and renames each based on its predicted class.
- Error Handling: skips files that cannot be identified as images.
- Configurable input size: allows setting the input size for resizing images before classification.

## Prerequisites
- TensorFlow (tensorflow) and PIL (pillow) libraries are required. Install them using:
```
pip install tensorflow pillow
```
- A trained TensorFlow Lite model (.tflite file).

## Parameters
- image_folder: the path to the folder containing the images to be classified.
- model_path: the path to the .tflite model file.
- input_size: a tuple representing the size to which each image is resized (e.g., (128, 128)).
- class_names: a list of class labels corresponding to the model's output.

## Description
The script loads a TensorFlow Lite model and uses it to classify images within a specified directory. For each image, the predicted class label is appended to the original filename, allowing easy identification and organization of images.

## Key Functions
### preprocess_image(image_path, input_size)
Prepares an image for model inference by resizing and normalizing it:
```
def preprocess_image(image_path, input_size):
    try:
        image = Image.open(image_path).convert('RGB')
        image = image.resize(input_size)
        image_array = np.array(image).astype(np.float32)
        image_array = image_array / 255.0
        image_array = np.expand_dims(image_array, axis=0)
        return image_array
    except UnidentifiedImageError:
        print(f"Skipping file {image_path}: Unidentified image format.")
        return None
```

### infer_image(image_array)
Runs the TFLite model inference on the processed image:
```
def infer_image(image_array):
    input_details = interpreter.get_input_details()[0]
    output_details = interpreter.get_output_details()[0]
    
    interpreter.set_tensor(input_details['index'], image_array)
    interpreter.invoke()
    
    output_data = interpreter.get_tensor(output_details['index'])
    return output_data
```

### get_class_label(output_data, class_names)
Determines the class label based on model output:
```
def rename_images(image_folder, class_names, input_size):
    if not os.path.exists(image_folder):
        print(f"Directory {image_folder} does not exist.")
        return
    
    files_processed = 0
    for filename in os.listdir(image_folder):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            image_path = os.path.join(image_folder, filename)
            image_array = preprocess_image(image_path, input_size)
            
            if image_array is not None:
                output_data = infer_image(image_array)
                class_label = get_class_label(output_data, class_names)
                
                new_filename = f"{class_label}_{filename}"
                new_image_path = os.path.join(image_folder, new_filename)
                
                os.rename(image_path, new_image_path)
                print(f"Renamed {filename} to {new_filename}")
                files_processed += 1
    
    if files_processed == 0:
        print(f"No images found in {image_folder} to process.")

input_size = (128, 128)
class_names = ["Class 1", "Class 2", "Class 3"]

print("Class names:", class_names)

image_folder = '/Users/path/to/model/check/images'
```

### rename_images(image_folder, class_names, input_size)
Processes all images in a folder, classifies them, and renames each file with the predicted class label:
```
def rename_images(image_folder, class_names, input_size):
    if not os.path.exists(image_folder):
        print(f"Directory {image_folder} does not exist.")
        return
    
    files_processed = 0
    for filename in os.listdir(image_folder):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            image_path = os.path.join(image_folder, filename)
            image_array = preprocess_image(image_path, input_size)
            
            if image_array is not None:
                output_data = infer_image(image_array)
                class_label = get_class_label(output_data, class_names)
                
                new_filename = f"{class_label}_{filename}"
                new_image_path = os.path.join(image_folder, new_filename)
                
                os.rename(image_path, new_image_path)
                print(f"Renamed {filename} to {new_filename}")
                files_processed += 1
    
    if files_processed == 0:
        print(f"No images found in {image_folder} to process.")

input_size = (128, 128)
class_names = ["Class 1", "Class 2", "Class 3"]

print("Class names:", class_names)

image_folder = '/Users/path/to/model/check/images'
```

### Main Functionality
Set the path for the image folder, the class names, and the input size for the images, then run the renaming process:
```    
    rename_images(image_folder, class_names, input_size)
```

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
