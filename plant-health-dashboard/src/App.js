import React, { useState, useEffect } from 'react';
import LiveVideo from './components/video';
import SensorData from './components/sensor';

function App() {
  const [sensorData, setSensorData] = useState({
    temperature: null,
    humidity: null,
    soil: null,
    light: null
  });

  useEffect(() => {
    // Fetch sensor data from Flask backend
    fetch("/api/sensor_data")
      .then(response => response.json())
      .then(data => {
        setSensorData(data);
      })
      .catch(error => {
        console.error("There was an error fetching the sensor data", error);
      });
  }, []);  // The empty dependency array ensures this runs once when the component mounts

  return (
    <div className="App">
      <h1>Plant Health Monitoring</h1>
      <LiveVideo />
      <SensorData title="Temperature" value={sensorData.temperature} unit="°F" />
      <SensorData title="Humidity" value={sensorData.humidity} unit="%" />
      <SensorData title="Soil Moisture" value={sensorData.soil} />
      <SensorData title="Light" value={sensorData.light} unit="lux" />
    </div>
  );
}

export default App;
