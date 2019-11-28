#!/usr/bin/python
import sys
import json

sys.path.append('.')
import scale_handler

SERVICE_NAME = 'ScaleInECSTaskCluster'
os.environ['STAGE'] = 'Staging'
os.environ['SLACK_URL'] = 'https://hooks.slack.com/services/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'
os.environ['SCALE_IN_THRESHOLD'] = 60
os.environ['DATAPOINT_PERIOD'] = 1
os.environ['DATAPOINT_COUNT'] = 1

scale_handler.trigger_scale_in(1, 2)
