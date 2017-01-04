#!/usr/bin/python3
"""
    Personal health improvement example
"""

import fitbit
import datetime

# insert your keys here
CONSUMER_KEY = "***REMOVED***"
CONSUMER_SECRET = "45ae7950f85f825638ff0e8087efad4"
ACCESS_TOKEN = "***REMOVED***"
REFRESH_TOKEN = "***REMOVED***"


if __name__ == "__main__":
    fbit_client = fitbit.Fitbit(CONSUMER_KEY,
                                CONSUMER_SECRET,
                                access_token=ACCESS_TOKEN,
                                refresh_token=REFRESH_TOKEN)
    now = datetime.datetime.now()
    end_time = now.strftime("%H:%M")
    response = fbit_client.intraday_time_series('activities/steps',
                                                period='1d')
    print(response['activities-steps'][0]['value'])
