#adding items to my Video-Game DynamoDB table
#Asonti Ginn
import boto3
ddb = boto3.client('dynamodb')

response = ddb.put_item(
    Item={
        'Game': {
            'S': 'Call of Duty MW2',
        },
        'Release-year': {
            'N': '2022',
        },
    },
    ReturnConsumedCapacity='TOTAL',
    TableName='Video_Game',
)

print(response)