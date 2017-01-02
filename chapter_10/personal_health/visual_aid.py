#!/usr/bin/python3
"""
    Visual aid to track personal fitness
"""

import blinkt
import time

if __name__ == "__main__":
    blinkt.set_brightness(0.1)
    for i in range(6):
        blinkt.set_pixel(i, 0, 255, 0)
    while True:
        blinkt.set_pixel(7, 255, 0, 0)
        blinkt.show()
        time.sleep(1)
        blinkt.set_pixel(7, 0, 0, 0)
        blinkt.show()
        time.sleep(1)
