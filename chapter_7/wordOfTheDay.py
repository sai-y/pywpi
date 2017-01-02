#!/usr/bin/python3

from wordnik import *

apiUrl = 'http://api.wordnik.com/v4'

if __name__ == "__main__":
  client = swagger.ApiClient(API_KEY, apiUrl)
  wordsApi = WordsApi.WordsApi(client)
  example = wordsApi.wordOfTheDay('2016-10-16')