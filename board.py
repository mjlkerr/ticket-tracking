from boto3 import resource
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime

board_table = resource('dynamodb').Table('Board')

def insert():
    response = board_table.put_item(
        Item={
            'Board_ID': 1, # Assuming Board_ID is the partition key
            'Sprint_ID': 123, # Assuming Sprint_ID is the sort key
            'Name': 'Martha123',
            'description': 'This is a sample board description.',
            'modified_at': datetime.now().isoformat()
        }
    )
    print("Insert response:", response)

insert()
