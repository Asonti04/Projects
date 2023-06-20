#Code for the lambda function
import json
import boto3
sqs = boto3.client('sqs')

def lambda_handler(event, context):
    response = sqs.send_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/867608235945/Shipped_Orders',
        MessageBody='#15634'
    )
    print(response)
    return 'Thank you for your purchase!'