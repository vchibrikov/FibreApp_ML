# Import packages
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import logging
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Suppress non-critical warnings
logging.getLogger("tensorflow").setLevel(logging.ERROR)

# Define variables
img_height, img_width = 64, 64
batch_size = 500
class_number = 3
epochs_number = 5

# Define paths
train_dir = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG_Android_3/TRAIN_BATCH'
test_dir = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG_Android_3/TEST_BATCH'
valid_dir = '/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG_Android_3/VALIDATION_BATCH'

# Read data
train_ds = tf.keras.utils.image_dataset_from_directory(
    train_dir, image_size=(img_height, img_width), batch_size=batch_size)
test_ds = tf.keras.utils.image_dataset_from_directory(
    test_dir, image_size=(img_height, img_width), batch_size=batch_size)
val_ds = tf.keras.utils.image_dataset_from_directory(
    valid_dir, image_size=(img_height, img_width), batch_size=batch_size)

# Normalize data for better performance
normalization_layer = tf.keras.layers.Rescaling(1./255)

train_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
val_ds = val_ds.map(lambda x, y: (normalization_layer(x), y))
test_ds = test_ds.map(lambda x, y: (normalization_layer(x), y))

# Define the base model with MobileNetV2
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(img_height, img_width, 3),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False

# Create the model
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(class_number, activation='softmax')
])

# Compile the model
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=['accuracy']
)

# Train the model without steps_per_epoch and validation_steps
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs_number
)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(test_ds)
print(f"Test accuracy: {test_accuracy * 100:.2f}%")

# Plot training & validation accuracy values
plt.figure(figsize=(8, 5))
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Plot training & validation loss values
plt.figure(figsize=(8, 5))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Convert to TFLite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TFLite model
with open("/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/MODELS/FibreAppML.tflite", "wb") as f:
    f.write(tflite_model)

print("Model conversion to TFLite completed and saved.")