import time
import board
import busio
import adafruit_bmp3xx
 
bmp.pressure_oversampling = 8
bmp.temperature_oversampling = 2


celsius = bmp.temperature
pascals = bmp.pressure
hPa = pascals * .01
inHg = pascals * 0.029529983071445
fahrenheit = (9.0/5.0) * celsius + 32

print(f'bmp280 celsius={celsius},fahrenheit={fahrenheit},hPa={hPa},inHg={inHg}')
