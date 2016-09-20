#!/usr/bin/python3

from urllib import request
from urllib.error import URLError

if __name__ == "__main__":
  # Source for link: http://stackoverflow.com/a/30635751/822170
  try:
    response = request.urlopen('http://nist.time.gv/actualtime.cgi')
    print(response.read())
  except URLError as error:
    print("Something went wrong. Try again")