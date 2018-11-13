# RaspberryPiZeroW-Weather- with Adafruit BMP388 Temp-Pressure-Altitude


<img src="https://cdn-shop.adafruit.com/970x728/3966-00.jpg" height="300"/><img src="https://cdn-shop.adafruit.com/1200x900/3966-02.jpg" height="300"/>

<div class="content">
<div class="page-title-wrapper">
<h1 class="headline">
<span id="pinouts">Pinouts</span>
</h1>
<div class="author">
<span class="name"></span>
</a> </div>
</div>
<div class="page-content">
<div class="row-fluid build-image">

<h2>Power Pins:</h2>
<ul>
<li>
<strong>Vin</strong> - this is the power pin. Since the sensor chip uses 3 VDC, we have included a voltage regulator on board that will take 3-5VDC and safely convert it down. To power the board, give it the same power as the logic level of your microcontroller - e.g. for a 5V micro like Arduino, use 5V</li>
<li>
<strong>GND</strong> - this is the Ground connect to ground on thr raspberry pi board </li>
</ul>
<h2>
<span class="fa fa-link"></span></a><span id="i2c-logic-pins-2-2" class="anchor-link-target"></span><span id="i2c-logic-pins" class="anchor-link-target"></span>I2C Logic pins:</h2>
<ul>
<li>
<strong>SCK </strong>- this is <em>also </em>the I2C clock pin, connect to your microcontrollers I2C clock line.</li>
<li>
<strong>SDI </strong>- this is <em>also</em> the I2C data pin, connect to your microcontrollers I2C data line.</li>
</ul>
</div>

---------------------------------------------------
On Your Rapspberry Pi Zero W

Enable I2C in the configuration menu 

* sudo raspi-config
   Go to interface section and select I2C to YES
* sudo apt-get update
* sudo apt-get upgrade
* sudo apt-get install i2c-tools python-pip
* pip3 install spidev
* pip3 install pow
* pip3 install RPi.GPIO
* pip3 install adafruit-blinka
* pip3 install board
* pip3 install smbus2
* sudo reboot
---------------------------------------------------
To Test I2C communication  

* sudo i2cdetect -y 1
* sudo i2cdump -y 1 0x77      
---------------------------------------------------
Now you need to clone 

git clone https://github.com/adafruit/Adafruit_CircuitPython_BMP3XX.git
---------------------------------------------------
* once it is copied to your Pi Board type 
* cd Adafruit_CircuitPython_BMP3XX
* then type sudo pyhton3 setup.py install

---------------------------------------------------
* then wget https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_BMP3XX/master/adafruit_bmp3xx.py
* then type python3 adafruit_bmp3xx.py
* then type python3 bmp388-6.py

---------------------------------------------------

