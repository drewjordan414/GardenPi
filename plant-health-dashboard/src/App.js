// import React, { useState, useEffect } from 'react';
// import { Container, AppBar, Toolbar, Typography, Grid, CssBaseline, Card, CardContent, Box } from '@material-ui/core';
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
//           {[
//             { title: "Temperature", value: sensorData.temperature, unit: "°F" },
//             { title: "Humidity", value: sensorData.humidity, unit: "%" },
//             { title: "Soil Moisture", value: sensorData.soil },
//             { title: "Light", value: sensorData.light, unit: "lux" }
//           ].map(sensor => (
//             <Grid item xs={6} sm={3} key={sensor.title}>
//               <Card>
//                 <CardContent>
//                   <SensorData title={sensor.title} value={sensor.value} unit={sensor.unit} />
//                 </CardContent>
//               </Card>
//             </Grid>
//           ))}
//         </Grid>
//       </Container>
//       <Box style={{ position: 'fixed', right: '1rem', bottom: '1rem' }}>
//         <Typography variant="body2">
//           Built with React by Drew
//         </Typography>
//       </Box>
//     </ThemeProvider>
//   );
// }

// export default App;

// added in graphs for sensor data
import React, { useState, useEffect } from 'react';
import { Container, AppBar, Toolbar, Typography, Grid, CssBaseline, Card, CardContent, Box } from '@material-ui/core';
import { createTheme, ThemeProvider } from '@material-ui/core/styles';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts';
import LiveVideo from './components/video';
import SensorData from './components/sensor';

const theme = createTheme({
  palette: {
    primary: {
      main: '#99A98F',
    },
    secondary: {
      main: '#C1D0B5',
    },
    background: {
      default: '#D6E8DB',
      paper: '#FFF8DE',
    },
    // error: {
    //   // main: '#ff7',
    // },
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
        const response = await fetch('http://localhost:5000/api/sensor_data');
        const data = await response.json();
        setSensorData(data);
      } catch (error) {
        console.error("Failed to fetch sensor data:", error);
      }
    };

    fetchSensorData();
  }, []);

  const mockData = [
    { name: 'Time1', temperature: sensorData.temperature, humidity: sensorData.humidity, soil: sensorData.soil, light: sensorData.light },
    // Add more data points as required for demonstration purposes
  ];

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

          <Grid item xs={12} sm={6}>
            {[
              { title: "Temperature", value: sensorData.temperature, unit: "°F" },
              { title: "Humidity", value: sensorData.humidity, unit: "%" },
              { title: "Soil Moisture", value: sensorData.soil },
              { title: "Light", value: sensorData.light, unit: "lux" }
            ].map(sensor => (
              <Card key={sensor.title} style={{ marginBottom: '15px' }}>
                <CardContent>
                  <SensorData title={sensor.title} value={sensor.value} unit={sensor.unit} />
                </CardContent>
              </Card>
            ))}
          </Grid>

          <Grid item xs={12} sm={6}>
            <Card>
              <CardContent>
                <Typography variant="h6">Temperature & Humidity</Typography>
                <LineChart width={400} height={150} data={mockData}>
                  <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Line type="monotone" dataKey="temperature" stroke="#8884d8" />
                  <Line type="monotone" dataKey="humidity" stroke="#82ca9d" />
                </LineChart>
              </CardContent>
            </Card>

            <Card style={{ marginTop: '15px' }}>
              <CardContent>
                <Typography variant="h6">Soil Moisture</Typography>
                <LineChart width={400} height={150} data={mockData}>
                  <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Line type="monotone" dataKey="soil" stroke="#ff7300" />
                </LineChart>
              </CardContent>
            </Card>

            <Card style={{ marginTop: '15px' }}>
              <CardContent>
                <Typography variant="h6">Light</Typography>
                <LineChart width={400} height={150} data={mockData}>
                  <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Line type="monotone" dataKey="light" stroke="#f34c56" />
                </LineChart>
              </CardContent>
            </Card>
          </Grid>
        </Grid>

        <Box style={{ position: 'fixed', right: '1rem', bottom: '1rem' }}>
          <Typography variant="body2">
            Built with React by Drew
          </Typography>
        </Box>
      </Container>
    </ThemeProvider>
  );
}

export default App;

