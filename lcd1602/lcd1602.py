import time
from machine import I2C, Pin


class LCD1602:

    def __init__(
            self,
            i2c_id=1, sda=Pin(26), scl=Pin(27),
            lcd_addr=0x27, light_on=True, freq=400_000
    ):
        """

        :param lcd_addr: LCD address
        :param i2c_id: I2C ID
        :param sda:
        :param scl:
        :param freq:
        """
        self.i2c = I2C(i2c_id, sda=sda, scl=scl, freq=freq)
        self.LCD_ADDR = lcd_addr
        self.light_status = light_on
        try:
            # LCD1602 初始化
            self.send(0x33)
            time.sleep(0.002)
            self.send(0x32)
            time.sleep(0.002)
            self.send(0x28)
            time.sleep(0.002)
            self.send(0x0C)
            time.sleep(0.002)
            self.send(0x01)
            self.turn_light()
        except Exception as e:
            print(f"初始化失败：{e}")
        else:
            print("初始化成功")

    def send(self, data: int, is_data=False):
        addr = self.LCD_ADDR
        tag = 0x04
        if is_data:
            addr |= 0x01
            tag = 0x05
        # 发送7-4位数据
        buf = data & 0xF0
        self.i2c.writeto(addr, bytes([buf | tag]))
        # time.sleep(0.002)
        self.i2c.writeto(addr, bytes([buf & 0xFB]))
        # 发送3-0位数据
        buf = (data & 0x0F) << 4
        self.i2c.writeto(addr, bytes([buf | tag]))
        # time.sleep(0.002)
        self.i2c.writeto(addr, bytes([buf & 0xFB]))
        # 重置灯光
        self.turn_light()

    def turn_light(self, on: bool = None):
        if on is not None:
            self.light_status = on
        if self.light_status:
            self.i2c.writeto(self.LCD_ADDR, bytes([0x08]))
        else:
            self.i2c.writeto(self.LCD_ADDR, bytes([0x00]))

    def clear(self):
        self.send(0x01)

    def show(self, x: int, y: int, text: str):
        x = max(0, min(x, 15))
        y = max(0, min(y, 1))
        self.send(0x80 + 0x40 * y + x)
        for c in text:
            self.send(ord(c), is_data=True)
