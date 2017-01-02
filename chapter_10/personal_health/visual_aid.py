#!/usr/bin/python3
"""
    Visual aid to track personal fitness
"""

import blinkt


if __name__ == "__main__":
    blinkt.set_brightness(0.1)
    for i in range(7):
        blinkt.set_pixel(i, 0, 255, 0)
        show()