import tensorflow as tf
import cv2
import numpy as np
import tensorflow_hub as hub
import json
import urllib.request

# Load the saved model from TensorFlow Hub
model = hub.load("https://tfhub.dev/rishit-dagli/plant-disease/1")

# Download and load the class indices
url = "https://github.com/Rishit-dagli/Greenathon-Plant-AI/releases/download/v0.1.0/class_indices.json"
class_indices = json.loads(urllib.request.urlopen(url).read().decode())

def preprocess_image(image, target_size=(224, 224)):
    """Preprocess the image for the model."""
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
    image = cv2.resize(image, target_size)
    image = tf.convert_to_tensor(image)
    image = tf.image.convert_image_dtype(image, tf.float32) / 255.0  # Normalize to [0,1]
    return tf.expand_dims(image, axis=0)

def predict_deficiency(image):
    """Predict the nutrient deficiency using the loaded model."""
    processed_image = preprocess_image(image)
    predictions = model(processed_image)
    predicted_class = tf.argmax(predictions, axis=1).numpy()[0]
    return class_indices[str(predicted_class)]

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
        label = predict_deficiency(frame)
        
        # Define color based on prediction. Here, just setting it to red for simplicity.
        color = (0, 0, 255)
        
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
