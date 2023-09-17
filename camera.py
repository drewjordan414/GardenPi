# housekeeping
import tensorflow as tf
import cv2
import numpy as np
import tensorflow_hub as hub
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
# Load the saved model
# model_path = 'model/saved_model.pb'
model = hub.load("https://www.kaggle.com/models/rishitdagli/plant-disease/frameworks/TensorFlow2/variations/plant-disease/versions/1")

# Optional: If the model has a specific signature for serving
# infer = model.signatures["serving_default"]

def capture_image_from_camera():
    """Capture image from the default camera and return it."""
    cap = cv2.VideoCapture(0)  # 0 for default camera
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    ret, frame = cap.read()
    cap.release()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        exit()
    return frame

def preprocess_image(image, target_size=(224, 224)):
    """Preprocess the image for the model."""
    image = cv2.resize(image, target_size)
    image = tf.convert_to_tensor(image)
    image = tf.image.convert_image_dtype(image, tf.float32)
    return tf.expand_dims(image, axis=0)  # Expand dims to make it a batch of size 1

def predict_deficiency(image):
    """Predict the nutrient deficiency using the loaded model."""
    processed_image = preprocess_image(image)
    predictions = model(processed_image)
    # Assuming model returns class probabilities
    predicted_class = tf.argmax(predictions, axis=1).numpy()[0]
    return predicted_class

if __name__ == "__main__":
    image = capture_image_from_camera()
    result = predict_deficiency(image)
    print(f"Predicted Nutrient Deficiency: {result}")

