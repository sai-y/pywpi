#!/usr/bin/python3
"""
    Personal health improvement example
"""

import fitbit
import datetime

# insert your keys here
CONSUMER_KEY = "229VMS"
CONSUMER_SECRET = "45ae7950f85f825638ff0e8087efad4c"
REFRESH_TOKEN = "995b32d720517141e69a5d577e5285d71c729be41589fb40b797a2f214b7e3b0"
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzTk1RQ1QiLCJhdWQiOiIyMjlWTVMiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJwcm8gcm51dCByc2xlIiwiZXhwIjoxNDgzNDE2OTYzLCJpYXQiOjE0ODMzODgxNjN9.jn6Zcxyi8NxuXMxFV4XOLp4t9LhDVzu515ktBO8SfFw"


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
