import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# Define image size and batch size
img_height, img_width = 128, 128
batch_size = 1000

# Load datasets
train_ds = tf.keras.utils.image_dataset_from_directory(
    "/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG_Android/TRAIN_BATCH",
    image_size=(img_height, img_width),
    batch_size=batch_size
)
val_ds = tf.keras.utils.image_dataset_from_directory(
    "/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG_Android/VALIDATION_BATCH",
    image_size=(img_height, img_width),
    batch_size=batch_size
)
test_ds = tf.keras.utils.image_dataset_from_directory(
    "/Users/vadymchibrikov/Desktop/FIBREAPP_IMAGES/ENG_Android/TEST_BATCH",
    image_size=(img_height, img_width),
    batch_size=batch_size
)

# Define class names
class_names = [
    "Apple", "Bean", "Beans", "Blueberry", "Carrot", "Champignon", "Cherry",
    "Chinese cabbage", "Cucumber", "Dill", "Eggplant", "Grapefruit (cv. Star Ruby)", 
    "Grapes (cv. Red Globe)", "Grapes (cv. Sultana)", "Lemon (cv. Primofiori)", 
    "Lime", "Orange", "Parsley", "Pear (cv. Conference)", "Pineapple", 
    "Radish", "Strawberry", "Tomato (cv. Tatami)", "Zucchini"]

# Visualize some training images
plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")

# Define the model architecture
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
    tf.keras.layers.Dense(24)  # Output layer for 24 classes
])

# Compile the model
model.compile(
    optimizer="adam",
    loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

# Train the model
model.fit(
    train_ds,              # Training dataset
    validation_data=val_ds,  # Validation dataset
    epochs=25              # Increase this number to train for more epochs
)

# Evaluate the model on the test dataset
model.evaluate(test_ds)

# Visualize predictions
plt.figure(figsize=(10, 10))
for images, labels in test_ds.take(1):
    classifications = model(images)
    
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        index = np.argmax(classifications[i])
        plt.title("Pred: " + class_names[index] + " | Real: " + class_names[labels[i]])
        plt.axis("off")

# Convert and save the model to a TFLite model
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
with open("model.tflite", 'wb') as f:
    f.write(tflite_model)