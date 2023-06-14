#Delete item then table
import boto3
ddb = boto3.client('dynamodb')
response = ddb.delete_item(
    Key={
        'Game': {
            'S': 'Cooking-mama',
        },
        'Release-year': {
            'N': '2006',
        },
    },
   TableName='Video_Game',
)

print(response)


#deletes table

response1 = ddb.delete_table(
    TableName='Video_Game'
)

print(response1)