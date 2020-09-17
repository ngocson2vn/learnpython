import argparse
from dms import client, describe_replication_tasks

target_tasks = [
  "ai-chat2analytics",
  "company-account-manager2analytics",
  "finc-connect2analytics",
  "finc-point2analytics",
  "fincapp-requl-mobile2analytics-important",
  "lifelog2analytics-normal-table",
  "lifelog2analytics-user-sensors-steps-counts",
  "sns-crawler2analytics",
  "wellness-survey2analytics",
  "activity-timeline2analytics",
  "fi-chat2analytics",
  "finc-payment2analytics",
  "grouper2analytics",
  "lifelog2analytics-big-table",
  "lifelog2analytics-big-table-2",
  "onboarding2analytics",
  "rankie2analytics",
  "wellness-ai2analytics"
]

tasks = describe_replication_tasks()

for t in target_tasks:
  for task in tasks:
    if (task['ReplicationTaskIdentifier'] == t) and task['Status'] == 'running':
      resp = client.stop_replication_task(ReplicationTaskArn=task['ReplicationTaskArn'])
      targetTask = resp['ReplicationTask']
      print(targetTask['ReplicationTaskIdentifier'], targetTask['Status'])
    elif task['ReplicationTaskIdentifier'] == t:
      print(task['ReplicationTaskIdentifier'], task['Status'])

