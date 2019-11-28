## Lambda functions perform scale-in ECS clusters StagingTask and ProductionTask
### Description
#### Lambda functions:
```
functions:
  trigger_scale_in:
    handler: scale_handler.trigger_scale_in
    events:
      - schedule: rate(1 hour)
  kill_daemon:
    handler: daemon_handler.kill_daemon
```
#### `trigger_scale_in`
This function checks `SCALE_IN_THRESHOLD` periodically. If the threshold crossed, it will call the lambda function `kill_daemon`. If the lambda function `kill_daemon` returns status `SUCCESS`, it will detach the oldest instance from the ECS cluster's AutoScalingGroup and decrement the desired capacity value by 1. Finally, it will terminate the detached instance.

#### `kill_daemon`
This function receives the oldest instance's IP address and ssh key as arguments from the lambda function `trigger_scale_in` and helps kill all daemons running in the target instance. Firstly, it does ssh into the target instance. Then, it downloads the program [kill_daemon](https://github.com/FiNCDeveloper/Dockerfiles/blob/ngocson2vn/kill_daemon/jenkins_scripts/scripts/kill_daemon.go) and executes this program to kill all running daemons.

#### Reference
The `kill_daemon` program: https://github.com/FiNCDeveloper/Dockerfiles/pull/210/files

### Setup
```
# Install nvm
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash
nvm install node
nvm use node

#Install serverless package
npm install -g serverless
```

### Deploy:
Note: Because the package `pycrypto` depends on some native libaries, you must use a Linux box to deploy these lambda functions.
```
pip install -t vendored/ -r requirements.txt
serverless deploy --stage staging
serverless deploy --stage production
```

### Set environment variables for lambda functions
Function `trigger_scale_in`
```
STAGE=Staging or Production
SLACK_URL=<incoming-webhook url>
SCALE_IN_THRESHOLD=60
DATAPOINT_PERIOD=15
DATAPOINT_COUNT=4
```

Function `kill_daemon`
```
STAGE=Staging or Production
RO_AWS_ID=<AWS_ACCESS_KEY_ID>
RO_AWS_KEY=<AWS_SECRET_ACCESS_KEY>
SLACK_POST_URL=<incoming-webhook url>
S3_KILL_DAEMON_PROG=s3://finc-ci-artifacts/jenkins_scripts/v2/master/bin/kill_daemon
```