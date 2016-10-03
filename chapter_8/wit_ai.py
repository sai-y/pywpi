#!/usr/bin/python3

import requests

if __name__ == "__main__":
  url = 'https://api.wit.ai/speech?v=20160526'
  headers = {"Authorization": "Bearer PYQ2OPAUWBB2MSUWVANLMC3FZ2ZB7U5O",
             "Content-Type": "audio/wav"}
  files = {'file': open('sp01.wav', 'rb')}
  response = requests.post(url, headers=headers, files=files)
  print(response.status)
  print(response.text)