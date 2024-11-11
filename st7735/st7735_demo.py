from machine import SPI
from st7735 import TFT
from sysfont import sysfont


spi = SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, sck=10, mosi=11)
tft = TFT(spi, 8, 9, 7)
tft.rotation(2)
tft.initr()
tft.rgb(True)
tft.fill(TFT.BLACK)
tft.text((10, 10), "Hello World!", TFT.RED, sysfont, 1, nowrap=True)