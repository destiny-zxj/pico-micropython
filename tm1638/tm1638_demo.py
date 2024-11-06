import math
import utime
from machine import Pin
from tm1638 import TM1638


tm = TM1638(stb=Pin(17), clk=Pin(18), dio=Pin(19))
tm.brightness(0)  # 亮度。0-7

while True:
    for i in range(8):
        utime.sleep_ms(200)
        tm.leds(0)  # 关闭所有 LED
        tm.led(i, 1)  # 点亮第 i 个 LED
        tm.show(f"LED {i+1}")  # 数码管显示
        k_v = tm.keys()  # 获取按键
        if k_v > 0:
            k = f"S{int(math.log(k_v, 2)) + 1}"
            print(f"key:", k)
