# GardenPi 🌱

Monitor your plant's health with live video analytics and various sensor readings such as temperature, humidity, soil moisture, and light. This system combines a frontend built with React to display the data and a backend Flask server to handle sensor readings and video stream processing.

## Features

- **Live Video Stream**: View a live feed of your plants with real-time analytics overlaying the video.
- **Sensor Data**: Real-time readings from various sensors:
  - Temperature (in Fahrenheit)
  - Humidity (in percentage)
  - Soil Moisture
  - Light (in lux)
  
- **Predictive Analysis**: Utilizing TensorFlow and TensorFlow Hub, the system can predict nutrient deficiencies from the live video feed.

## Prerequisites

- Python 3.8+
- Node.js and npm

## Getting Started

### Backend Setup

1. **Clone the Repository**:
    ```
    git clone https://github.com/your-username/plant-health-monitoring.git
    cd plant-health-monitoring
    ```

2. **Set Up a Virtual Environment**:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```
    pip install -r requirements.txt
    ```

4. **Run the Flask App**:
    ```
    python app.py
    ```

### Frontend Setup

1. Navigate to the React app directory:
    ```
    cd path-to-react-app
    ```

2. Install the required npm packages:
    ```
    npm install
    ```

3. Start the React app:
    ```
    npm start
    ```

Visit `http://localhost:3000` in your browser to access the web application.

## Technologies Used

- **Backend**:
  - Flask
  - TensorFlow and TensorFlow Hub
  - OpenCV
  - Adafruit libraries for sensor integration

- **Frontend**:
  - React
  - Material-UI

## Contributions

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](LICENSE)
