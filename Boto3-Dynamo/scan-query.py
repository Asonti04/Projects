#4. SCAN & QUERY
#Asonti Ginn
import boto3
ddb = boto3.client('dynamodb')
response = ddb.scan(
    TableName='Video_Game',
)

print(response)

response2 = ddb.query(
    TableName='Video_Game',
    ExpressionAttributeValues={
        ':Game': {
            'S': 'Sims4',
        },
    },
    KeyConditionExpression='Game = :Game'
)

print(response2)
