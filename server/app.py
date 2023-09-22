from flask import Flask, Response, jsonify
import cv2
import board
import busio 
from adafruit_seesaw.seesaw import Seesaw
import adafruit_sht4x
import adafruit_tsl2591
from flask_cors import CORS

# Initialize I2C sensors 
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize Seesaw soil sensor
try:
    ss = Seesaw(i2c, addr=0x36)
    ss_available = True
    print("Seesaw soil sensor initialized.")
except Exception as e:
    ss = None
    ss_available = False
    print("Failed to initialize Seesaw soil sensor:", str(e))

# Initialize SHT4x temperature and humidity sensor
try:
    sht = adafruit_sht4x.SHT4x(i2c)
    sht_available = True
    print("SHT4x sensor initialized.")
except Exception as e:
    sht = None
    sht_available = False
    print("Failed to initialize SHT4x sensor:", str(e))

# Initialize TSL2591 light sensor
try:
    tsl = adafruit_tsl2591.TSL2591(i2c)
    tsl_available = True
    print("TSL2591 light sensor initialized.")
except Exception as e:
    tsl = None
    tsl_available = False
    print("Failed to initialize TSL2591 light sensor:", str(e))


app = Flask(__name__)
CORS(app)  # Handling CORS for local development

def read_temp():
    """Read the temperature in Fahrenheit from the SHT40."""
    if sht_available:
        return sht.temperature * 1.8 + 32
    else:
        return None
def read_humidity():
    """Read the humidity from the SHT40."""
    if sht_available:
        return sht.relative_humidity
    else:
        return None

def read_soil():
    """Read the soil moisture from the soil sensor."""
    if ss_available:
        return ss.moisture_read()
    else:
        return None

def read_light():
    """Read the light sensor value."""
    if tsl_available:
        return tsl.lux
    else:
        return None

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
