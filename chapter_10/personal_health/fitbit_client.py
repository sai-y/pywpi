#!/usr/bin/python3
"""
    Personal health improvement example
"""

import fitbit
import datetime

# insert your keys here
CONSUMER_KEY = "229VMS"
CONSUMER_SECRET = "45ae7950f85f825638ff0e8087efad4"
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzTk1RQ1QiLCJhdWQiOiIyMjlWTVMiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJwcm8gcm51dCByc2xlIiwiZXhwIjoxNDgzNTM0MzQ4LCJpYXQiOjE0ODM1MDU1NDh9._RQtxVktitZ-l-m1dNMDmXDPoPIUm7TG_w2BFFczAXg"
REFRESH_TOKEN = "6cd0e37f7ee88a30ce883c9b83c6a3804164e99e68fb81f1fb7ae2c7402c89fa"


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
