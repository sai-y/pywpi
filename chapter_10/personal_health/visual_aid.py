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
CONFIG_FILE = '/home/pi/config.ini'
config = configparser.ConfigParser()
config.read(CONFIG_FILE)

CONSUMER_KEY = config.get("APP", "CONSUMER_KEY")
CONSUMER_SECRET = config.get("APP", "CONSUMER_SECRET")
REFRESH_TOKEN = config.get("USER", "REFRESH_TOKEN")
ACCESS_TOKEN = config.get("USER", "ACCESS_TOKEN")


def update_tokens(token):

    if (
        token['access_token'] != ACCESS_TOKEN or
        token['refresh_token'] != REFRESH_TOKEN
    ):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        config.set("USER", "REFRESH_TOKEN", token['refresh_token'])
        config.set("USER", "ACCESS_TOKEN", token['access_token'])

        with open(CONFIG_FILE, "w") as config_file:
            config.write(config_file)


def get_steps(client):
    """
        Return the steps logged
    """
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
            return -1
    return num_steps


def get_goal(client):
    """
        Determine Daily step goal
    """
    num_steps = 0

    try:
        response = client.activities_daily_goal()
    except Exception as error:
        print(error)

    return response['goals']['steps']


if __name__ == "__main__":

    client = fitbit.Fitbit(CONSUMER_KEY,
                           CONSUMER_SECRET,
                           access_token=ACCESS_TOKEN,
                           refresh_token=REFRESH_TOKEN,
                           refresh_cb=update_tokens)

    blinkt.set_brightness(0.1)
    current_time = time.time()

    # retrieve steps
    steps = get_steps(client)
    denominator = int(get_goal(client) / 8)
    num_leds = steps // denominator

    while True:
        # update steps every 15 minutes
        if (time.time() - current_time) > 900:
            steps = get_steps(client)
            # make another attempt only if step check was successful
            if steps >= 0:
                current_time = time.time()
                num_leds = steps // denominator
            else:
                continue

            for i in range(8):
                blinkt.set_pixel(i, 0, 0, 0)
                blinkt.set_brightness(0.1)
                blinkt.show()

        if num_leds > 8:
            num_leds = 8

        for i in range(num_leds):
            blinkt.set_pixel(i, 0, 255, 0)
            blinkt.set_brightness(0.1)
            blinkt.show()

        if num_leds <= 7:
            blinkt.set_pixel(num_leds, 255, 0, 0)
            blinkt.set_brightness(0.1)
            blinkt.show()
            time.sleep(1)
            blinkt.set_pixel(num_leds, 0, 0, 0)
            blinkt.set_brightness(0.1)
            blinkt.show()
            time.sleep(1)
