from flask import Flask, jsonify, Response, render_template
import cv2
import numpy as np
from io import BytesIO

app = Flask(__name__)

# Initialize your sensors and model here...

@app.route('/sensors', methods=['GET'])
def get_sensor_data():
    # Read your sensor values
    temp = read_temp()
    humidity = read_humidity()
    soil = read_soil()
    light = read_light()
    
    # Return as JSON
    return jsonify({
        'temperature': temp,
        'humidity': humidity,
        'soil': soil,
        'light': light
    })

@app.route('/camera', methods=['GET'])
def get_camera_frame():
    ret, frame = cap.read()
    if not ret:
        return "Error capturing frame", 500

    # Predict and annotate the frame
    result = predict_deficiency(frame)
    label = "Healthy" if result == 0 else "Not Healthy"
    # ... (annotate the frame as in your code)

    # Convert the frame to JPEG and return
    buffer = BytesIO()
    cv2.imwrite(buffer, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    return Response(buffer.getvalue(), mimetype='image/jpeg')

@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)
