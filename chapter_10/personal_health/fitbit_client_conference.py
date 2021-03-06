#!/usr/bin/python3
"""
    Personal health improvement example
"""

import fitbit
import datetime
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


if __name__ == "__main__":
    fbit_client = fitbit.Fitbit(CONSUMER_KEY,
                                CONSUMER_SECRET,
                                access_token=ACCESS_TOKEN,
                                refresh_token=REFRESH_TOKEN)
    # now = datetime.datetime.now()
    # end_time = now.strftime("%H:%M")
    response = fbit_client.time_series(
        'activities/steps',
        user_id='5HX8YP',
        period='1d'
    )
    
