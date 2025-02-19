import boto3
import json
import time

# Initialize Kinesis client
kinesis_client = boto3.client('kinesis')
STREAM_NAME = 'demo-stream'

def lambda_handler(event, context):
    try:
        # Generate a unique record ID
        record_id = str(int(time.time()))
        
        # Create the data record
        data = {
            'id': record_id,
            'timestamp': str(int(time.time())),
            'value': event.get('value', 0),
            'type': event.get('type', 'default')
        }
        
        # Put the record into Kinesis
        response = kinesis_client.put_record(
            StreamName=STREAM_NAME,
            Data=json.dumps(data),
            PartitionKey=record_id
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Record successfully sent to Kinesis',
                'data': data,
                'kinesis_response': response
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': f'Error in lambda execution: {str(e)}'
            })
        }
