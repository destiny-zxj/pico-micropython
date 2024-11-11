import os
from machine import SPI, Pin
from lcd1602 import LCD1602


lcd = LCD1602()
lcd.clear()
lcd.show(0, 0, '123456')
