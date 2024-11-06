from machine import Pin, I2C
from at24c256 import AT24C256

i2c = I2C(0, freq=10000, sda=Pin(16), scl=Pin(17))
it = AT24C256(i2c)

