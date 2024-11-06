""" AT24C256, 256kbit (32768 bytes / 32 KB), 512 pages, 64 bytes per page, i2c addr 0x50 """
import time

class AT24C256(object):

    def __init__(self, i2c, i2c_addr=0x50, pages=512, bpp=64):
        self.i2c = i2c
        self.i2c_addr = i2c_addr
        self.pages = pages
        self.bpp = bpp
        self.addrsize = 16

    def capacity(self):
        """Storage capacity in bytes"""
        return self.pages * self.bpp

    def read(self, start, length):
        buf = b''
        for i in range(length):
            buf += self.i2c.readfrom_mem(self.i2c_addr, start + i, 1, addrsize=self.addrsize)
        return buf

    def write(self, start, data):
        for i in range(len(data)):
            self.i2c.writeto_mem(self.i2c_addr, start+i, data[i], addrsize=self.addrsize)
            time.sleep_ms(5)


