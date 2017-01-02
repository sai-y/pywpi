#!/usr/bin/python3
"""
    Visual aid to track personal fitness
"""

import blinkt
import datetime
import fitbit
import time

# insert your keys here
CONSUMER_KEY = "229VMS"
CONSUMER_SECRET = "45ae7950f85f825638ff0e8087efad4c"
REFRESH_TOKEN = "bbb3dea74025ca96270f4f594c9a3deccc06f9f2afcbc1ca2e24ad8f9bd8ffa9"
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzTk1RQ1QiLCJhdWQiOiIyMjlWTVMiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJwcm8gcm51dCByc2xlIiwiZXhwIjoxNDgzNDEyOTk3LCJpYXQiOjE0ODMzODQxOTd9.D_IDFQEfEJumlUo34nEe1qoqSFnyOdUV3vA0YBwbsRA"


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
