#!/usr/bin/python3

import requests

URL = "http://feeds.bayareabikeshare.com/stations/stations.json"

if __name__ == "__main__":
  response = requests.get(URL)
  print(response.json())