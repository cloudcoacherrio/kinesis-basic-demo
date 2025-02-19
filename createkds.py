import boto3 

def create_kinesis_stream(): 
    kinesis_client = boto3.client('kinesis') 
    try: 
        kinesis_client.create_stream( 
            StreamName='demo-stream', 
            ShardCount=1 
        ) 
        print("Stream created successfully") 
    except kinesis_client.exceptions.ResourceInUseException: 
        print("Stream already exists") 

# Run this locally to create the stream 
create_kinesis_stream() 
