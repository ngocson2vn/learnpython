import argparse
from dms import client, describe_replication_tasks

START_TYPE = 'resume-processing'

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--task-id", required=True, help="(Required) ReplicationTaskIdentifier")
targetTaskId = vars(parser.parse_args())['task_id']
print("ReplicationTaskIdentifier = {}\n".format(targetTaskId))

tasks = describe_replication_tasks()
for task in tasks:
  if (targetTaskId == 'ALL' or targetTaskId == task['ReplicationTaskIdentifier']) and task['Status'] == 'stopped':
    resp = client.start_replication_task(
      ReplicationTaskArn=task['ReplicationTaskArn'],
      StartReplicationTaskType=START_TYPE
    )
    targetTask = resp['ReplicationTask']
    print(targetTask['ReplicationTaskIdentifier'], targetTask['Status'])
  else:
    print(task['ReplicationTaskIdentifier'], task['Status'])

print("Total tasks: {}".format(len(tasks)))
