import argparse
from dms import client, describe_replication_tasks

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--task-id", required=True, help="(Required) ReplicationTaskIdentifier")
targetTaskId = vars(parser.parse_args())['task_id']
print("ReplicationTaskIdentifier = {}\n".format(targetTaskId))

tasks = describe_replication_tasks()
for task in tasks:
  if (task['ReplicationTaskIdentifier'] == targetTaskId or targetTaskId == 'ALL') and task['Status'] == 'running':
    resp = client.stop_replication_task(ReplicationTaskArn=task['ReplicationTaskArn'])
    targetTask = resp['ReplicationTask']
    print(targetTask['ReplicationTaskIdentifier'], targetTask['Status'])
  else:
    print(task['ReplicationTaskIdentifier'], task['Status'])
print("Total tasks: {}".format(len(tasks)))
