#!/usr/bin/python3

from urllib import request


# access google.com
with request.urlopen('http://nist.time.gov/actualtime.cgi') as response:
  print(response.read())