#Create a sqs
import boto3
sqs = boto3.client('sqs')

response = sqs.create_queue(QueueName='Shipped_Orders')

print(response)