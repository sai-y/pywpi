#!/usr/bin/python3

import requests
import json

URL = 'https://hooks.slack.com/services/'

if __name__ == "__main__":
  payload = {"text": "The cat door was just opened!"}
  try:
    response = requests.post(URL, json.dumps(payload))
    print(response.text)
  except requests.exceptions.ConnectionError as error:
    print("The error is %s" % error)
