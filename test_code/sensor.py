import board
import busio 
import adafruit_seesaw
import adafruit_sht4x
import adafruit_tsl2591
from time import sleep
from random import randrange


# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
ss = adafruit_seesaw.Seesaw(i2c)
sht = adafruit_sht4x.SHT4x(i2c)
tsl = adafruit_tsl2591.TSL2591(i2c)

# Create a function to read the temperature from the SHT40
def read_temp():
    # read the temperature in Fahrenheit
    return sht.temperature * 1.8 + 32

# Create a function to read the humidity from the SHT40
def read_humidity():
    return sht.relative_humidity

# Create a function to read the soil moisture from the soil sensor
def read_soil():
    return ss.moisture_read()

# Function to read the light sensor 
def read_light():
    return tsl.lux

print("Starting the sensors...")
print("Reading the sensor values...")

value = 0 
while True:
    value = (value + randrange(0, 10)) % 100
    print('sending data: ', value)
    sleep(3)
    break

# Output the sensor data
while True:
    # Read and print the temperature
    temperature = read_temp()
    print("Temperature: ", temperature)
    
    # Print humidity
    print("Humidity: ", read_humidity())

    # Print soil moisture
    print("Soil Moisture: ", read_soil())
    
    # Print light value
    print("Light: ", read_light())
