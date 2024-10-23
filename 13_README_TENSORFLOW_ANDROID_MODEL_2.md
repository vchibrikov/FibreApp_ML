# 13_TENSORFLOW_ANDROID_MODEL_2.py
This Python script trains a simple convolutional neural network (CNN) for image classification using TensorFlow, visualizes sample images, evaluates the trained model, and converts it to a TensorFlow Lite format for deployment. It is designed for beginners to understand the flow of data preparation, model training, and inference.

- Visual Studio Code release used: 1.93.1
- Python release used: 3.12.4 (64-bit)
> Warning: There are no guarantees this code will run on your machine.

## Features
- Data loading & visualization: loads training, validation, and testing image datasets from directories and displays sample images with labels.
- Custom CNN model: a straightforward convolutional neural network (CNN) is defined for image classification.
- Model training & evaluation: trains the CNN using training data, validates it with validation data, and evaluates accuracy with test data.
- Prediction visualization: shows predictions vs. actual labels for a batch of test images.
- TFLite model conversion: converts the trained model into a TensorFlow Lite (.tflite) format for deployment on mobile or edge devices.

## Prerequisites
- TensorFlow (tensorflow) and Matplotlib (matplotlib) libraries are required. Install them using:
```
pip install tensorflow matplotlib
```
- Properly structured training, validation, and testing datasets.

## Parameters
- img_height and img_width: the dimensions to which each image will be resized.
- batch_size: number of images per batch for training.
- epochs: number of training epochs.
- class_names: list of class labels corresponding to the categories of images.

## Description
The script defines a CNN model for image classification, normalizes the image data, and trains the model using specified datasets. After training, the model is evaluated on test data, and a few example predictions are visualized alongside actual labels. The trained model is then converted to a .tflite format, making it suitable for use on devices with limited resources.

## Key Functions
### Data loading and visualization
Loads datasets and displays a grid of sample images with their respective labels:
```
train_ds = tf.keras.utils.image_dataset_from_directory(
    "/Users/path/to/train/data",
    image_size=(img_height, img_width),
    batch_size=batch_size
)
# Similar functions are used for val_ds and test_ds
```
```
# Visualizes 9 images from the training dataset:
plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")
```

### Model Architecture - defining a simple CNN model:
```
model = tf.keras.Sequential([
    tf.keras.layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
    tf.keras.layers.Conv2D(128, 3, activation="relu"),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(128, 3, activation="relu"),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(128, 3, activation="relu"),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense()
])
```
### Model Training and Evaluation
Compiles and trains the model using the Adam optimizer and sparse categorical cross-entropy loss:
```
model.compile(
    optimizer="adam",
    loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)
model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs
)
```

### Evaluates the model's performance on the test dataset:
```
model.evaluate(test_ds)
```

### Prediction Visualization - visualization of model predictions vs. actual labels:
```
plt.figure(figsize=(10, 10))
for images, labels in test_ds.take(1):
    classifications = model(images)
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        index = np.argmax(classifications[i])
        plt.title("Pred: " + class_names[index] + " | Real: " + class_names[labels[i]])
        plt.axis("off")
```

### TFLite Model Conversion
Converts the trained model to a TensorFlow Lite format:
```
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
with open("model.tflite", 'wb') as f:
    f.write(tflite_model)
```

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
