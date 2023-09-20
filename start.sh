#!/bin/bash

# Start the Flask backend
# cd /home/drewjordan/GardenPi/backend
# relative path
cd backend
flask run &

# Start the React frontend
# cd /home/drewjordan/GardenPi/plant-health-dashboard
# realtive path
cd plant-health-dashboard
npm start &

# Wait for all child processes to finish
wait
