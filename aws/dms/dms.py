import boto3

client = boto3.client('dms')

def describe_replication_task(replicationTaskArn):
  response = client.describe_replication_tasks(
    Filters=[
        {
            'Name': 'replication-task-arn',
            'Values': [
                replicationTaskArn,
            ]
        },
    ]
  )

  if 'ReplicationTasks' in response and len(response['ReplicationTasks']) == 1:
    return response['ReplicationTasks'][0]

  return None

def describe_replication_tasks(marker=''):
  all_tasks = []
  response = client.describe_replication_tasks(
    Marker=marker,
    MaxRecords=20
  )

  all_tasks.extend(response['ReplicationTasks'])
  if 'Marker' in response and len(response['Marker']) > 0:
    tasks = describe_replication_tasks(response['Marker'])
    all_tasks.extend(tasks)

  return all_tasks