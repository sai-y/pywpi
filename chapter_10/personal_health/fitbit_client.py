#!/usr/bin/python3
"""
    Personal health improvement example
"""

import fitbit
import datetime

# insert your keys here
CONSUMER_KEY = "***REMOVED***"
CONSUMER_SECRET = "***REMOVED***"
REFRESH_TOKEN = "686c3eadf248fef7b783e53aa7f36a083d10c39aefc8ead831da049f6599c377"
ACCESS_TOKEN = "***REMOVED***"


if __name__ == "__main__":
    fbit_client = fitbit.Fitbit(CONSUMER_KEY,
                                CONSUMER_SECRET,
                                access_token=ACCESS_TOKEN,
                                refresh_token=REFRESH_TOKEN)
    now = datetime.datetime.now()
    end_time = now.strftime("%H:%M")
    response = fbit_client.intraday_time_series('activities/steps',
                                                detail_level='15min',
                                                start_time="00:00",
                                                end_time=end_time)
    print(response['activities-steps'][0]['value'])
