import utime
from machine import Pin
from ir import read_code, send_code, validate_code, InvalidCodeException
from ir_keys import ir_keys

pin_in = Pin(5, Pin.IN, Pin.PULL_UP)
# pin_out = Pin(21, mode=Pin.OUT)

while True:
    out = read_code(pin_in)
    # ignore random signals 
    if out:
        try:
            validate_code(out)
            # print(type(out), out)
            for item in ir_keys:
                if out == item[0]:
                    print(item[1])
            # utime.sleep(3)
            # send_code(pin_out, out)
        except InvalidCodeException:
            print("InvalidCodeException:" + out)