from Adafruit_IO import Client, Feed, Block, Dashboard, Layout
import board
import busio 
import adafruit_seesaw
import adafruit_sht4x
import time 
import adafruit_tsl2591

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL,board.SDA)
ss = adafruit_seesaw(i2c)
sht = adafruit_sht4x.SHT4x(i2c)
tsl = adafruit_tsl2591.TSL2591(i2c)

# Create a function to read the temperature from the SHT40
def read_temp():
    # read the temperature in Fahrenheit
    return sht.temperature * 1.8 *32

# Create a function to read the humidity from the SHT40
def read_humidity():
    return sht.relative_humidity

# create a function to read the soil moisture from the soil sensor
def read_soil():
    return ss.moisture_read()

# function to read the light sensor 
def read_light():
    return tsl.lux

# Create a aio instance using the username and key
aio_usermname = "YOUR_ADAFRUIT_IO_USERNAME"
aio_key = "YOUR_ADAFRUIT_IO_KEY"
aio = Client(aio_usermname, aio_key)

# Create a feed
temperature_feed = aio.feeds('temperature')
humiditiy_feed = aio.feeds('humidity')
soil_feed = aio.feeds('soil')
light_feed = aio.feeds('light')

# create a guage for the sensors
temperature_guage = aio.feeds('temperature-guage')
humidity_gauge = aio.feeds('humidity-guage')
soil_gauge = aio.feeds('soil-guage')
light_gauge = aio.feeds('light-gauge')

# create a block for the sensors
temperature_block = aio.feeds('temperature-block')
hmidity_block = aio.feeds('humidity-block')
soil_block = aio.feeds('soil-block')
light_block = aio.feeds('light-block')


print("Starting the sensors...")
print("Reading the sensor values...")
while True:
    # read the temperature
    temperature = read_temp()
    print("Temperature: ", temperature)
    # send the temperature to the temperature feed
    aio.send_data(temperature_feed.key, read_temp())
    # send the humdiity to the humidity guage
    aio.send_data(humidity_gauge.key, read_humidity())
    # send the soil moisture to the soil guage
    aio.send_data(soil_gauge.key, read_soil())
    # send the light to the light guage
    aio.send_data(light_gauge.key, read_light())



