#bmp388-6.py
import time
import board
import busio
import adafruit_bmp3xx

i2c = busio.I2C(board.SCL, board.SDA)
bmp388 = adafruit_bmp3xx.BMP3XX_I2C(i2c)

bmp388.pressure_oversampling = 2
bmp388.temperature_oversampling = 2
bmp388.altitude_oversampling = 2

bmp388.sea_level_pressure = 1017.1 #(Sea level Pressure )1013.25

#    degrees        =    bmp388.temperature()
#    degrees        =   (degrees * 1.8) + 32
#    pascals        =    bmp388._pressure()
#    inchesHG       =   (pascals /3386.39)
#    mbar           =   (inchesHG * 33.8639)
#    hectopascals   =   (pascals / 100)
#    altitude       =    bmp388.altitude()
#    degrees2       =    bmp388.temperature()

#    print 'Temperature    = {0:0.2f} deg F'.format(degrees)
#    print 'Temperature    = {0:0.2f} deg C'.format(degrees2)
#    print 'Pressure       = {0:0.2f} inHg'.format(inchesHG)
#    print 'Pressure       = {0:0.2f} Mbar' .format(mbar)
#    print 'Pressure       = {0:0.2f} hPa  '.format(pascal)

while True:
    print("--------------------------")
    print("Temperature:  {0:0.2f} Deg C ".format(bmp388.temperature))
    print("Pressure:     {:6.3f}  HpA   ".format(bmp388.pressure))
    print("Altitude:     {0:0.4f} Meters ".format(bmp388.altitude))
    time.sleep(1)

