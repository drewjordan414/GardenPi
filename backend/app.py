# from flask import Flask, Response, jsonify
# import cv2
# import board
# import busio 
# import adafruit_seesaw
# import adafruit_sht4x
# import adafruit_tsl2591
# import tensorflow as tf
# import numpy as np
# import tensorflow_hub as hub
# from flask_cors import CORS
# import openai
# import dotenv
# # Initialize OpenAI API read from env file
# api_key = dotenv.get_key('.env, API_KEY')

# # Initialize I2C sensors 
# i2c = busio.I2C(board.SCL, board.SDA)
# ss = adafruit_seesaw.Seesaw(i2c)
# sht = adafruit_sht4x.SHT4x(i2c)
# tsl = adafruit_tsl2591.TSL2591(i2c)

# # Load the saved model
# model = hub.load("https://tfhub.dev/rishit-dagli/plant-disease/1")

# app = Flask(__name__)
# CORS(app)  # Handling CORS for local development

# def openai_chat(query):
#     """Query the OpenAI API and return the response."""
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=query,
#         temperature=0.9,
#         max_tokens=150,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0.6,
#         stop=["\n", " Human:", " AI:"]
#     )
#     return response.choices[0].text


# def read_temp():
#     """Read the temperature in Fahrenheit from the SHT40."""
#     return sht.temperature * 1.8 + 32

# def read_humidity():
#     """Read the humidity from the SHT40."""
#     return sht.relative_humidity

# def read_soil():
#     """Read the soil moisture from the soil sensor."""
#     return ss.moisture_read()

# def read_light():
#     """Read the light sensor value."""
#     return tsl.lux

# @app.route('/api/sensor_data')
# def sensor_data():
#     """Provide sensor data as a JSON response."""
#     data = {
#         "temperature": read_temp(),
#         "humidity": read_humidity(),
#         "soil": read_soil(),
#         "light": read_light()
#     }
#     return jsonify(data)

# def preprocess_image(image, target_size=(224, 224)):
#     """Preprocess the image for the model."""
#     image = cv2.resize(image, target_size)
#     image = tf.convert_to_tensor(image)
#     image = tf.image.convert_image_dtype(image, tf.float32)
#     return tf.expand_dims(image, axis=0)  # Expand dims to make it a batch of size 1

# def predict_deficiency(image):
#     """Predict the nutrient deficiency using the loaded model."""
#     processed_image = preprocess_image(image)
#     predictions = model(processed_image)
#     # Assuming model returns class probabilities
#     predicted_class = tf.argmax(predictions, axis=1).numpy()[0]
#     return predicted_class

# def gen():
#     """Generate the video stream."""
#     cap = cv2.VideoCapture(0)
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Can't receive frame (stream end?). Exiting ...")
#             break

#         # Get the prediction for the frame
#         result = predict_deficiency(frame)
        
#         # Display the result on the frame
#         label = "Healthy" if result == 0 else "Not Healthy"
#         color = (0, 255, 0) if label == "Healthy" else (0, 0, 255)
        
#         height, width, _ = frame.shape
#         top_left = (int(width * 0.05), int(height * 0.05))
#         bottom_right = (int(width * 0.95), int(height * 0.15))
#         cv2.rectangle(frame, top_left, bottom_right, color, -1)
#         cv2.putText(frame, label, (int(width * 0.1), int(height * 0.12)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
#         # Convert the frame to JPEG and return
#         ret, jpeg = cv2.imencode('.jpg', frame)
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

# @app.route('/api/video_feed')
# def video_feed():
#     """Video streaming route."""
#     return Response(gen(),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)



# version with no prediction
from flask import Flask, Response, jsonify
import cv2
import board
import busio 
import adafruit_seesaw
import adafruit_sht4x
import adafruit_tsl2591
from flask_cors import CORS

# Initialize I2C sensors 
i2c = busio.I2C(board.SCL, board.SDA)
ss = adafruit_seesaw.Seesaw(i2c)
sht = adafruit_sht4x.SHT4x(i2c)
tsl = adafruit_tsl2591.TSL2591(i2c)

app = Flask(__name__)
CORS(app)  # Handling CORS for local development

def read_temp():
    """Read the temperature in Fahrenheit from the SHT40."""
    return sht.temperature * 1.8 + 32

def read_humidity():
    """Read the humidity from the SHT40."""
    return sht.relative_humidity

def read_soil():
    """Read the soil moisture from the soil sensor."""
    return ss.moisture_read()

def read_light():
    """Read the light sensor value."""
    return tsl.lux

@app.route('/api/sensor_data')
def sensor_data():
    """Provide sensor data as a JSON response."""
    data = {
        "temperature": read_temp(),
        "humidity": read_humidity(),
        "soil": read_soil(),
        "light": read_light()
    }
    return jsonify(data)

def gen():
    """Generate the video stream."""
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        
        # Convert the frame to JPEG and return
        ret, jpeg = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

@app.route('/api/video_feed')
def video_feed():
    """Video streaming route."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
