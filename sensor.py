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

# Create a aio instance using the username and key
aio_usermname = "YOUR_ADAFRUIT_IO_USERNAME"
aio_key = "YOUR_ADAFRUIT_IO_KEY"
aio = Client(aio_usermname, aio_key)

# Create a feed
temperature_feed = aio.feeds('temperature')
humiditiy_feed = aio.feeds('humidity')
soil_feed = aio.feeds('soil')
light_feed = aio.feeds('light')


