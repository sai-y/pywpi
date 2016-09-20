#!/usr/bin/python3

from urllib import request


# access google.com
with request.urlopen('http://time.nist.gov') as response:
  print(response.read())