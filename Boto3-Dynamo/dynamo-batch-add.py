#3. BATCH PLACING DYNAMODB ITEMS
#Asonti Ginn 
import boto3
ddb = boto3.client('dynamodb')
response = ddb.batch_write_item(
    RequestItems={
        'Video_Game': [
            {
                'PutRequest': {
                    'Item': {
                        'Game': {
                            'S': 'Sims4',
                        },
                        'Release-year': {
                            'N': '2014',
                        },
                    
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Game': {
                            'S': 'Battlefield-6',
                        },
                        'Release-year': {
                            'N': '2021',
                        },
                        
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Game': {
                            'S': 'Spiderman',
                        },
                        'Release-year': {
                            'N': '2020',
                        },
                        
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Game': {
                            'S': 'Minecraft',
                        },
                        'Release-year': {
                            'N': '2011',
                        },
                        
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Game': {
                            'S': 'Roblox',
                        },
                        'Release-year': {
                            'N': '2006',
                        },
                        
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Game': {
                            'S': 'Fortnite',
                        },
                        'Release-year': {
                            'N': '2017',
                        },
                        
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Game': {
                            'S': 'Cooking-mama',
                        },
                        'Release-year': {
                            'N': '2006',
                        },
                        
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Game': {
                            'S': 'Mario',
                        },
                        'Release-year': {
                            'N': '1983',
                        },
                        
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Game': {
                            'S': 'Crash-Bandicoot',
                        },
                        'Release-year': {
                            'N': '1996',
                        },
                        
                    },
                },
            },
        ],
    },
)

print(response)
