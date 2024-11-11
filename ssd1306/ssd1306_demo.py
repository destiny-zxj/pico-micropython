from machine import Pin, I2C
from ssd1306 import SSD1306_I2C


i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=100000, timeout=5000000)

led = SSD1306_I2C(128, 64, i2c)

led.text('hello', 5, 15)
led.show()
