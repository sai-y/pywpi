#!/usr/bin/python3
"""
    Personal health improvement example
"""

import fitbit
import json
import datetime

# insert your keys here
CONSUMER_KEY = "229VMS"
CONSUMER_SECRET = "45ae7950f85f825638ff0e8087efad4c"
REFRESH_TOKEN = "bbb3dea74025ca96270f4f594c9a3deccc06f9f2afcbc1ca2e24ad8f9bd8ffa9"
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzTk1RQ1QiLCJhdWQiOiIyMjlWTVMiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJwcm8gcm51dCByc2xlIiwiZXhwIjoxNDgzMzYyNjIzLCJpYXQiOjE0ODMzMzM4MjN9.cdUihcllL6D_c9Pgm_zLlYabiwacxXk1Shap-hVzNLA"


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
