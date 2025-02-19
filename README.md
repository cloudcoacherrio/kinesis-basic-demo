# Kinesis Data Stream to DynamoDB Basic Demo

## Overview
This lab demonstrates a simple data streaming pipeline using AWS Kinesis Data Stream, Lambda functions, and DynamoDB.

## Prerequisites
- AWS Management Console Account
- IAM user with permissions for:
  - Kinesis Data Streams
  - Amazon DynamoDB
  - AWS Lambda
  - IAM
- Python 3
- boto3 library
- AWS CLI

## 1. Local Environment Preparation
Create and prepare your local Python environment:
# Install boto3
pip install boto3
# Optional: Create virtual environment
```bash
python3 -m venv myenv
source myenv/bin/activate
```
# Authenticate into AWS via AWS CLI
Create a programmatic user with Access Keys (with permissions listed under Prerequisites)  
Authenticate via IDE stored locally  

## 2. Create AWS Resources
Create the necessary AWS resources:

Create Kinesis Data Stream  
`python3 createkds.py`

Create DynamoDB Table  
`python3 createkdsbasictable.py`

## 3. Create Lambda Functions
Producer Lambda function  
`Upload kdsbasicproducer.py`

Create Role for the Producer Lambda function  
`Attach IAM policy using producerlambda.json`

Assign the execution role to the Producer Lambda function

Consumer Lambda Function  
`Upload kdsbasicconsumer.py`

Create Role for the Consumer Lambda function  
`Attach IAM policy using consumerlambda.json`

Add Kinesis stream as trigger  

## 4. Test Pipeline
In the Producer Lambda function, go to Test tab  
Create new test using `producerlambdatest.json`  
Run test  
Verify data in DynamoDB table  

## Configuration Notes
Replace REGION and ACCOUNT_ID in JSON policy files  
Verify stream name: demo-stream  
Verify DynamoDB table name: kds-basic-table  

## Troubleshooting
Check Lambda function logs for detailed error information  
Verify IAM role permissions  
Confirm all resource names match exactly  

## Clean Up
To avoid ongoing charges:

Delete Lambda functions  
Delete Kinesis Data Stream  
Delete DynamoDB table  
Remove IAM roles  

## Architecture
[Test Event] → [Producer Lambda] → [Kinesis Data Stream] → [Consumer Lambda] → [DynamoDB Table]  

## Best Practices
Use least privilege principle for IAM roles  
Monitor Lambda function performance  
Set up CloudWatch alarms for stream and function errors  
