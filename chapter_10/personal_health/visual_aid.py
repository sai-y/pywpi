#!/usr/bin/python3
"""
    Visual aid to track personal fitness
"""

import blinkt
import datetime
import fitbit
import time

# insert your keys here
CONSUMER_KEY = "***REMOVED***"
CONSUMER_SECRET = "***REMOVED***"
REFRESH_TOKEN = "***REMOVED***"
ACCESS_TOKEN = "***REMOVED***"

if __name__ == "__main__":
    fbit_client = fitbit.Fitbit(CONSUMER_KEY,
                                CONSUMER_SECRET,
                                access_token=ACCESS_TOKEN,
                                refresh_token=REFRESH_TOKEN)
    blinkt.set_brightness(0.1)
    for i in range(7):
        blinkt.set_pixel(i, 0, 255, 0)
    while True:
        now = datetime.datetime.now()
        end_time = now.strftime("%H:%M")
        response = fbit_client.intraday_time_series('activities/steps',
                                                    detail_level='15min',
                                                    start_time="00:00",
                                                    end_time=end_time)
        blinkt.set_pixel(7, 255, 0, 0)
        blinkt.show()
        time.sleep(1)
        blinkt.set_pixel(7, 0, 0, 0)
        blinkt.show()
        time.sleep(1)
