import boto3
import json
import base64

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
TABLE_NAME = 'kds-basic-table'  # Make sure this matches your DynamoDB table name
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    output = []
    failed_records = []
    
    try:
        # Process each record from Kinesis
        for record in event['Records']:
            try:
                # Kinesis data is base64 encoded
                payload = base64.b64decode(record['kinesis']['data'])
                data = json.loads(payload)
                
                # Store in DynamoDB
                store_in_dynamodb(data)
                
                # Add the processed record to output
                output.append(data)
                
            except Exception as record_error:
                failed_records.append({
                    'data': data if 'data' in locals() else None,
                    'error': str(record_error)
                })
                continue

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'Successfully processed {len(output)} records',
                'processed_records': output,
                'failed_records': failed_records
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': f'Error: {str(e)}'
            })
        }

def store_in_dynamodb(data):
    """
    Store the record in DynamoDB table
    """
    try:
        response = table.put_item(
            Item={
                'id': data['id'],  # Partition key
                'timestamp': data['timestamp'],
                'value': data['value'],
                'type': data['type']
            }
        )
        return response
        
    except Exception as e:
        raise Exception(f"Failed to store item in DynamoDB: {str(e)}")
