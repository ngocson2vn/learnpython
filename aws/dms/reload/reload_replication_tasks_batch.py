import argparse

import sys
sys.path.append('..')
import dms

START_TYPE = 'reload-target'


target_tasks = [
  "personal-supplement2analytics",
  "personal-supplement2analytics-bigtables",
  "tsubaki-staging2analytics"
]

tasks = dms.describe_replication_tasks()

for t in target_tasks:
  for task in tasks:
    if (task['ReplicationTaskIdentifier'] == t) and (task['Status'] in ['stopped', 'error', 'failed']):
      resp = dms.client.start_replication_task(
        ReplicationTaskArn=task['ReplicationTaskArn'],
        StartReplicationTaskType=START_TYPE
      )
      targetTask = resp['ReplicationTask']
      print(targetTask['ReplicationTaskIdentifier'], targetTask['Status'])
    elif task['ReplicationTaskIdentifier'] == t:
      print(task['ReplicationTaskIdentifier'], task['Status'])

