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
    client = fitbit.Fitbit(CONSUMER_KEY,
                           CONSUMER_SECRET,
                           access_token=ACCESS_TOKEN,
                           refresh_token=REFRESH_TOKEN)
    blinkt.set_brightness(0.1)
    current_time = time.time()

    num_leds = 0

    while True:
        # update steps every 15 minutes
        if (time.time() - current_time) > 900:
            try:
                now = datetime.datetime.now()
                end_time = now.strftime("%H:%M")
                response = client.intraday_time_series('activities/steps',
                                                       detail_level='15min',
                                                       start_time="00:00",
                                                       end_time=end_time)
            except Exception as error:
                print(error)
            else:
                current_time  = time.time()
                steps = response['activities-steps'][0]['value']
                num_leds = steps // 1250
                print(steps)
        
        if num_leds > 8:
            num_leds = 8
        
        for i in range(num_leds):
            blinkt.set_pixel(i, 0, 255, 0)
        
        if num_leds <= 7: 
            blinkt.set_pixel(num_leds, 255, 0, 0)
            blinkt.show()
            time.sleep(1)
            blinkt.set_pixel(num_leds, 0, 0, 0)
            blinkt.show()
            time.sleep(1)
