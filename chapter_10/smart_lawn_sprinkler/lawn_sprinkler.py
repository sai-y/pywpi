#!/usr/bin/python3
"""
    Smart Water Sprinkler Example
"""

import requests
import schedule
import time

URL = ("https://api.darksky.net/forecast/key"
       "/37.8267,-122.4233?exclude=currently,minutely,hourly")


def check_weather():
    try:
        response = requests.get(URL)
    except Exception as error:
        print(error)
    else:
        if response.status_code == 200:
            data = response.json()
            return data["daily"]["data"][1]["icon"] == "rain"


def turn_on_sprinkler():
    if not check_weather():
        # turn on sprinkler
        print("Turning on sprinkler")
        time.sleep(600)
        # turn off sprinkler
        print("Turning off sprinkler")
    else:
        print("Ignoring the sprinker for today")


def turn_off_sprinkler():
    pass


if __name__ == "__main__":
    schedule.every().day.at("22:27").do(turn_on_sprinkler)

    while True:
        schedule.run_pending()
        time.sleep(1)
