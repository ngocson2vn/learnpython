import boto3

def call_function(functionName, payload):
	client = boto3.client('lambda')
	response = client.invoke(
		FunctionName=functionName,
		InvocationType='RequestResponse',
		LogType='Tail',
		Payload=payload
	)

	return response