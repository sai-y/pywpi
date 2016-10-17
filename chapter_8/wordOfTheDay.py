#!/usr/bin/python3

from wordnik import *

API_KEY = 'c17e17b7d601024c8450e09f0830206b9d12c91729fa15a2c'
apiUrl = 'http://api.wordnik.com/v4'

if __name__ == "__main__":
  client = swagger.ApiClient(API_KEY, apiUrl)
  wordsApi = WordsApi.WordsApi(client)
  example = wordsApi.wordOfTheDay('2016-10-16')