# TENSOLFLOW_ANDROID_MODEL_1.py
This Python script trains an image classification model using TensorFlow's MobileNetV2 architecture on custom datasets, evaluates its performance, and converts the trained model into a TensorFlow Lite format (.tflite) for deployment on edge devices. It includes data preprocessing, training, validation, testing, and visualization of training progress.

- Visual Studio Code release used: 1.93.1
- Python release used: 3.12.4 (64-bit)
> Warning: There are no guarantees this code will run on your machine.

## Features
- Image classification model training: utilizes the MobileNetV2 architecture with pre-trained ImageNet weights as the base model, fine-tuning it for custom classification tasks.
- Data preprocessing: normalizes image data and prepares datasets for training, validation, and testing.
- Model evaluation: evaluates the model on a test dataset and displays the test accuracy.
- Performance visualization: plots training and validation accuracy and loss over epochs to track the model’s learning progress.
- TFLite model conversion: converts the trained model to a TensorFlow Lite format for efficient deployment on mobile and edge devices.

## Prerequisites
- TensorFlow (tensorflow) and Matplotlib (matplotlib) libraries are required. Install them using:
```
pip install tensorflow matplotlib
```
- Properly structured training, testing, and validation datasets in the specified directories.

## Parameters
- train_dir: the path to the directory containing training images.
- test_dir: the path to the directory containing testing images.
- valid_dir: the path to the directory containing validation images.
- img_height and img_width: the dimensions to which all images will be resized.
- batch_size: the number of images per batch for training.
- class_number: the number of classes in the dataset.
- epochs_number: the number of epochs for training the model.

## Description
The script uses transfer learning with the MobileNetV2 architecture, which is pre-trained on the ImageNet dataset. It adapts the model for custom image classification tasks by adding fully connected layers. It normalizes the image data, trains the model using training and validation datasets, and evaluates its accuracy on a test dataset. After training, the model is converted into a .tflite file, making it suitable for deployment in low-resource environments.

## Key Functions
### Data loading and preprocessing
Loads image datasets from directories and normalizes them:
```
train_ds = tf.keras.utils.image_dataset_from_directory(
    train_dir, image_size=(img_height, img_width), batch_size=batch_size)
# Similar functions are used for test_ds and val_ds
```

### Model building
Defines the model architecture using MobileNetV2 as a base:
```
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(img_height, img_width, 3),
    include_top=False,
    weights='imagenet'
)
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(class_number, activation='softmax')
])
```

### Model training and evaluation
Trains the model and evaluates its accuracy on the test dataset:
```
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs_number
)
test_loss, test_accuracy = model.evaluate(test_ds)
print(f"Test accuracy: {test_accuracy * 100:.2f}%")
```

### Performance visualization
Visualizes training accuracy and loss:
```
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
# Similar plotting is done for loss
```

### TFLite model conversion
Converts the trained model to a TensorFlow Lite model:
```
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
with open("/Users/path/to/save/model.tflite", "wb") as f:
    f.write(tflite_model)
```

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
