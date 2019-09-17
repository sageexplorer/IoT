from __future__ import print_function
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table_name = "iots"
table = dynamodb.create_table(
    TableName = table_name,
    KeySchema=[
        {
            'AttributeName': 'time',
            'KeyType': 'HASH'  #Partition key
        },

    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'message',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("Table status:", table.table_status)
