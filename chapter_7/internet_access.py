#!/usr/bin/python3

from urllib import request

# Source for link: http://stackoverflow.com/a/30635751/822170
with request.urlopen('http://nist.time.gov/actualtime.cgi') as response:
  print(response.read())