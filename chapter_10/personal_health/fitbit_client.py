#!/usr/bin/python3
"""
    Personal health improvement example
"""

import fitbit
import datetime
import configparser

# config is loaded from config file
# alternatively you may store them as constants in your program
config = configparser.ConfigParser()
config.read('config.ini')

CONSUMER_KEY = config.get("APP", "CONSUMER_KEY")
CONSUMER_SECRET = config.get("APP", "CONSUMER_SECRET")
REFRESH_TOKEN = config.get("USER", "REFRESH_TOKEN")
ACCESS_TOKEN = config.get("USER", "ACCESS_TOKEN")


if __name__ == "__main__":
    fbit_client = fitbit.Fitbit(CONSUMER_KEY,
                                CONSUMER_SECRET,
                                access_token=ACCESS_TOKEN,
                                refresh_token=REFRESH_TOKEN)
    now = datetime.datetime.now()
    end_time = now.strftime("%H:%M")
    response = fbit_client.intraday_time_series('activities/steps',
                                            detail_level='15min',
                                            start_time="00:00",
                                            end_time=end_time)
    print(response['activities-steps'][0]['value'])
