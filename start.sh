#!/bin/bash

# Start the Flask backend
cd backend
sudo flask run &

wait

# Go back to GardenPi directory
cd ..

# Start the React frontend
cd dashboard
sudo npm start &

# Wait for all child processes to finish
wait

