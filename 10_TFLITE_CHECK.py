import tensorflow as tf
import numpy as np
from PIL import Image, UnidentifiedImageError
import os

interpreter = tf.lite.Interpreter(model_path = "/Users/path/to/model.tflite")
interpreter.allocate_tensors()

print("TFLite model loaded successfully.")

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

def infer_image(image_array):
    input_details = interpreter.get_input_details()[0]
    output_details = interpreter.get_output_details()[0]
    
    interpreter.set_tensor(input_details['index'], image_array)
    interpreter.invoke()
    
    output_data = interpreter.get_tensor(output_details['index'])
    return output_data

def get_class_label(output_data, class_names):
    class_index = np.argmax(output_data)
    return class_names[class_index]

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

rename_images(image_folder, class_names, input_size)
