#!/usr/bin/python3
"""
    Smart Water Sprinkler Example
"""

import requests
import schedule


URL = ("https://api.darksky.net/forecast/***REMOVED***"
"/37.8267,-122.4233?exclude=currently,minutely,hourly")

if __name__ == "__main__":
	response = requests.get(URL)
	data = response.json()
	print(data["daily"]["data"][1]["rain"])