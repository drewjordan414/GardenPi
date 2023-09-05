# housekeeping 
import os
import cv2 
import time 
from time import sleep
# import the necessary packages
# from picamera.array import PiRGBArray
# from picamera import PiCamera

# setup the camera
camera = cv2.VideoCapture("/dev/video0") # ----> use cd /dev && ls to find the video device
cv2.VideoCapture(0) # ----> use this if you are using a webcam on device 0 
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# camera.resolution = (640, 480)
camera.framerate = 32
