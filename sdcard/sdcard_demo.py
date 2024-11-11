import os
from machine import SPI, Pin
from sdcard import SDCard


spi = SPI(0, baudrate=1000000, polarity=0, phase=0, bits=8, sck=18, mosi=19, miso=16)
sd = SDCard(spi, Pin(17))
vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')
print(os.listdir('/sd'))
