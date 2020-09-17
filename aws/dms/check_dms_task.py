import boto3

client = boto3.client('dms')

TASK_STATUS_RUNNING = 'running'

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



tasks = describe_replication_tasks()
errorMessages = []
for task in tasks:
  if task['Status'] == TASK_STATUS_RUNNING:
    if int(task['ReplicationTaskStats']['TablesErrored']) > 0:
      message = 'DMS Task: {}\nTask Status: {}\nThe number of corrupted tables: {}'.format(
                  task['ReplicationTaskIdentifier'],
                  'Running with errors',
                  int(task['ReplicationTaskStats']['TablesErrored'])
                )
      errorMessages.append(message)
if len(errorMessages) > 0:
  print('\n\n'.join(errorMessages))
