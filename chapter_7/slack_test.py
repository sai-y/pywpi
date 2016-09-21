#!/usr/bin/python3

import requests
import json

URL = 'https://hooks.slack.com/services/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'

if __name__ == "__main__":
  payload = {"text": "The cat door just opened!"}
  try:
    response = requests.post(URL, json.dumps(payload))
    print(response.text)
  except requests.exceptions.ConnectionError as error:
    print("The error is %s" % error)
