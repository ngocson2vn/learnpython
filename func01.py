#!/usr/bin/python

def check(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print "%s == %s" %(key,value)

check(api_key='DATADOG_APIKEY1', app_key='DATADOG_APPKEY1')
