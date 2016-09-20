#!/usr/bin/python3

from urllib import request


# access google.com
with request.urlopen('http://www.google.com') as response:
  print(response.read())