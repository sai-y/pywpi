#!/usr/bin/python3
"""
	Personal health improvement example
"""

import fitbit
import json
import datetime

# insert your keys here
CONSUMER_KEY = "***REMOVED***"
CONSUMER_SECRET = "***REMOVED***"
REFRESH_TOKEN = "***REMOVED***"
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
