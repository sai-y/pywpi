#!/usr/bin/python3

import requests

if __name__ == "__main__":
  url = 'https://api.wit.ai/speech?v=20161002'
  headers = {"Authorization": "Bearer PYQ2OPAUWBB2MSUWVANLMC3FZ2ZB7U5O",
             "Content-Type": "audio/wav"}
  files = open('sp02.wav', 'rb')
  response = requests.post(url, headers=headers, data=files)
  print(response.status_code)
  print(response.text)