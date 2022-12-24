#!/usr/bin/env python

#
#Mass unfollow friends on twitter
#

# Author
#  - Scott Mcintyre <me@scott.cm>
#  - http://scott.cm
#
# Usage
#
# Get your keys from https://dev.twitter.com/
# Ensure it has write access
# Change the api key values marked ##### below with the twitter keys
# Install http://code.google.com/p/python-twitter/

import twitter
import time

api = twitter.Api(consumer_key='PLACE_HOLDER', consumer_secret='PLACE_HOLDER', access_token_key='PLACE_HOLDER', access_token_secret='PLACE_HOLDER')

start = time.time()
i = 0
friends=api.GetFriendIDs()

try:
    for u in friends:
        print "Deleting %s" % (u)
        api.DestroyFriendship(u);
        i += 1

except:
    print "Possibly Rate limited? sleeping 60 seconds"
    time.sleep(60)

elapsed = (time.time() - start)
print "Deleted %s friends in %0.2f seconds" % (str(i), elapsed)
