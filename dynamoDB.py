#DynamoDB creation using boto3
#Asonti Ginn

import boto3
ddb = boto3.client('dynamodb')
response = ddb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Game',
            'AttributeType': 'S',
        },
          {
            'AttributeName': 'Release-year',
            'AttributeType': 'N',
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'Game',
            'KeyType': 'HASH',
        },
        {
            'AttributeName': 'Release-year',
            'KeyType': 'RANGE',
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 20,
        'WriteCapacityUnits': 20,
    },
    TableName= 'Video_Game',
)
print(response)