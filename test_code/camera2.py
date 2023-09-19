# housekeeping
import tensorflow as tf
import cv2
import numpy as np
import tensorflow_hub as hub
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

# Load the saved model
model = hub.load("https://www.kaggle.com/models/rishitdagli/plant-disease/frameworks/TensorFlow2/variations/plant-disease/versions/1")

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

def show_live_feed_with_prediction():
    """Show live feed and display prediction on captured frame."""
    cap = cv2.VideoCapture(0)  # 0 for default camera
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        
        # Get the prediction for the frame
        result = predict_deficiency(frame)
        
        # Display the result on the frame
        label = "Healthy" if result == 0 else "Not Healthy"  # Modify this line based on your model's output
        color = (0, 255, 0) if label == "Healthy" else (0, 0, 255)
        
        height, width, _ = frame.shape
        top_left = (int(width * 0.05), int(height * 0.05))
        bottom_right = (int(width * 0.95), int(height * 0.15))
        cv2.rectangle(frame, top_left, bottom_right, color, -1)
        cv2.putText(frame, label, (int(width * 0.1), int(height * 0.12)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Show the frame with the prediction
        cv2.imshow('Plant Health Detection', frame)
        
        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_live_feed_with_prediction()
# housekeeping
import tensorflow as tf
import cv2
import numpy as np
import tensorflow_hub as hub
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

# Load the saved model
model = hub.load("https://www.kaggle.com/models/rishitdagli/plant-disease/frameworks/TensorFlow2/variations/plant-disease/versions/1")

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

def show_live_feed_with_prediction():
    """Show live feed and display prediction on captured frame."""
    cap = cv2.VideoCapture(0)  # 0 for default camera
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        
        # Get the prediction for the frame
        result = predict_deficiency(frame)
        
        # Display the result on the frame
        label = "Healthy" if result == 0 else "Not Healthy"  # Modify this line based on your model's output
        color = (0, 255, 0) if label == "Healthy" else (0, 0, 255)
        
        height, width, _ = frame.shape
        top_left = (int(width * 0.05), int(height * 0.05))
        bottom_right = (int(width * 0.95), int(height * 0.15))
        cv2.rectangle(frame, top_left, bottom_right, color, -1)
        cv2.putText(frame, label, (int(width * 0.1), int(height * 0.12)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Show the frame with the prediction
        cv2.imshow('Plant Health Detection', frame)
        
        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_live_feed_with_prediction()
