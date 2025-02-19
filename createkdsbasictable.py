import boto3

def create_dynamodb_table():
    dynamodb = boto3.client('dynamodb')
    try:
        response = dynamodb.create_table(
            TableName='kds-basic-table',
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        print("Table created successfully")
    except dynamodb.exceptions.ResourceInUseException:
        print("Table already exists")

# Run this locally to create the table
create_dynamodb_table()
