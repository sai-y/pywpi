#!/usr/bin/python3

import requests
import json 

# generate your own url
APP_ID = '5d6f02fd4472611a20f4ce602010ee0c'
ZIP = 94103
URL = """http://api.openweathermap.org/data/2.5/weather?zip={}&appid={}\
      &units=imperial""".format(ZIP, APP_ID)

if __name__ == "__main__":
  # API Documentation: http://openweathermap.org/current#current_JSON
  try:
    # encode data payload and post it
    response = requests.get(URL)
    print(response.text)
  except requests.exceptions.ConnectionError as error:
    print("The error is %s" % error)
