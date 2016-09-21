#!/usr/bin/python3

import requests

if __name__ == "__main__":
  # Source for link: http://stackoverflow.com/a/30635751/822170
  try:
    response = requests.get('http://nist.time.gv/actualtime.cgi')
    print(response.read())
  except requests.HTTPError as error:
    print("Something went wrong. Try again")