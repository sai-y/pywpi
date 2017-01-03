#!/usr/bin/python3
"""
    Smart Water Sprinkler Example
"""

import requests
import schedule
import time

URL = ("https://api.darksky.net/forecast/08b2b3024c2a1b85dabf14cea653c899"
"/37.8267,-122.4233?exclude=currently,minutely,hourly")

def check_weather():
	try:
		response = requests.get(URL)
		print response.status_code
	except Exception as error:
		print(error)
	else:
		if response.status_code == 200:
			data = response.json()
			if data["daily"]["data"][1]["icon"] == "rain":
				return True
			else:
				return False

def turn_on_sprinkler():
	if not check_weather():
		# turn on sprinkler
		time.sleep(600)
		# turn off sprinkler
	else:
		print("Ignoring the sprinker for today")

def turn_off_sprinkler():
	pass

if __name__ == "__main__":
	check_weather()
	schedule.every().day.at("18:45").do(turn_on_sprinkler)

	while True:
		schedule.run_pending()
		time.sleep(1)