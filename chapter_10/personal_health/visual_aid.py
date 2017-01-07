#!/usr/bin/python3
"""
    Visual aid to track personal fitness
"""

import blinkt
import datetime
import fitbit
import time
import configparser

# config is loaded from config file
# alternatively you may store them as constants in your program
config = configparser.ConfigParser()
config.read('config.ini')

CONSUMER_KEY = config.get("APP", "CONSUMER_KEY")
CONSUMER_SECRET = config.get("APP", "CONSUMER_SECRET")
REFRESH_TOKEN = config.get("USER", "REFRESH_TOKEN")
ACCESS_TOKEN = config.get("USER", "ACCESS_TOKEN")


def refresh_token():
    global REFRESH_TOKEN
    oauth = fitbit.FitbitOauth2Client(client_id=CONSUMER_KEY,
                                      client_secret=CONSUMER_SECRET,
                                      refresh_token=REFRESH_TOKEN,
                                      access_token=ACCESS_TOKEN)
    REFRESH_TOKEN = oauth.refresh_token()


def get_steps():
    num_steps = 0

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
        str_steps = response['activities-steps'][0]['value']
        print(str_steps)
        try:
            num_steps = int(str_steps)
        except ValueError:
            pass
    return num_steps

if __name__ == "__main__":

    client = fitbit.Fitbit(CONSUMER_KEY,
                           CONSUMER_SECRET,
                           access_token=ACCESS_TOKEN,
                           refresh_token=REFRESH_TOKEN)

    blinkt.set_brightness(0.1)
    current_time = time.time()

    num_leds = 0
    steps = get_steps()

    while True:
        # update steps every 15 minutes
        if (time.time() - current_time) > 900:
            current_time = time.time()
            steps = get_steps()

        num_leds = steps // 1250

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
