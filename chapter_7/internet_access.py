#!/usr/bin/python3

import urllib 

if __name__ == "__main__":
  # Source for link: http://stackoverflow.com/a/30635751/822170
  try:
    response = urllib.request.urlopen('http://nist.time.gv/actualtime.cgi')
    print(response.read())
  except urllib.error.URLError as error:
    print("Something went wrong. Try again")