#!/usr/bin/python3

import requests

URL = "http://feeds.bayareabikeshare.com/stations/stations.json"

if __name__ == "__main__":
  # fetch the bike share information
  response = requests.get(URL)
  parsed_data = response.json()
  print(parsed_data['stationBeanList'][2])