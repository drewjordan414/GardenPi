// import React, { useState, useEffect } from 'react';
// import { Container, AppBar, Toolbar, Typography, Grid, CssBaseline } from '@material-ui/core';
// import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
// import LiveVideo from './components/video';
// import SensorData from './components/sensor';

// const theme = createMuiTheme({
//   palette: {
//     primary: {
//       main: '#404258',
//     },
//     secondary: {
//       main: '#50577A',
//     },
//     background: {
//       default: '#6B728E',
//       paper: '#474E68',
//     },
//   },
//   typography: {
//     // Adjust typography settings here if needed
//   },
// });

// function App() {
//   const [sensorData, setSensorData] = useState({
//     temperature: null,
//     humidity: null,
//     soil: null,
//     light: null
//   });

//   useEffect(() => {
//     const fetchSensorData = async () => {
//       try {
//         const response = await fetch('http://localhost:5000/api/sensor_data');  // Assuming Flask server runs on localhost:5000
//         const data = await response.json();
//         setSensorData(data);
//       } catch (error) {
//         console.error("Failed to fetch sensor data:", error);
//       }
//     };

//     fetchSensorData();
//   }, []);

//   return (
//     <ThemeProvider theme={theme}>
//       <CssBaseline />
//       <Container>
//         <AppBar position="static">
//           <Toolbar>
//             <Typography variant="h6">
//               Plant Health Monitoring
//             </Typography>
//           </Toolbar>
//         </AppBar>
        
//         <Grid container spacing={3}>
//           <Grid item xs={12}>
//             <LiveVideo />
//           </Grid>
//           <Grid item xs={6} sm={3}>
//             <SensorData title="Temperature" value={sensorData.temperature} unit="°F" />
//           </Grid>
//           <Grid item xs={6} sm={3}>
//             <SensorData title="Humidity" value={sensorData.humidity} unit="%" />
//           </Grid>
//           <Grid item xs={6} sm={3}>
//             <SensorData title="Soil Moisture" value={sensorData.soil} />
//           </Grid>
//           <Grid item xs={6} sm={3}>
//             <SensorData title="Light" value={sensorData.light} unit="lux" />
//           </Grid>
//         </Grid>
//       </Container>
//     </ThemeProvider>
//   );
// }

// export default App;

import React, { useState, useEffect } from 'react';
import { Container, AppBar, Toolbar, Typography, Grid, CssBaseline, Card, CardContent } from '@material-ui/core';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import LiveVideo from './components/video';
import SensorData from './components/sensor';

const theme = createMuiTheme({
  palette: {
    primary: {
      main: '#404258',
    },
    secondary: {
      main: '#50577A',
    },
    background: {
      default: '#6B728E',
      paper: '#474E68',
    },
  },
  typography: {
    // Adjust typography settings here if needed
  },
});

function App() {
  const [sensorData, setSensorData] = useState({
    temperature: null,
    humidity: null,
    soil: null,
    light: null
  });

  useEffect(() => {
    const fetchSensorData = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/sensor_data');  // Assuming Flask server runs on localhost:5000
        const data = await response.json();
        setSensorData(data);
      } catch (error) {
        console.error("Failed to fetch sensor data:", error);
      }
    };

    fetchSensorData();
  }, []);

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container>
        <AppBar position="static">
          <Toolbar>
            <Typography variant="h6">
              Plant Health Monitoring
            </Typography>
          </Toolbar>
        </AppBar>
        
        <Grid container spacing={3}>
          <Grid item xs={12}>
            <LiveVideo />
          </Grid>
          {[
            { title: "Temperature", value: sensorData.temperature, unit: "°F" },
            { title: "Humidity", value: sensorData.humidity, unit: "%" },
            { title: "Soil Moisture", value: sensorData.soil },
            { title: "Light", value: sensorData.light, unit: "lux" }
          ].map(sensor => (
            <Grid item xs={6} sm={3} key={sensor.title}>
              <Card>
                <CardContent>
                  <SensorData title={sensor.title} value={sensor.value} unit={sensor.unit} />
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      </Container>
    </ThemeProvider>
  );
}

export default App;

