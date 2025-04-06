from boto3 import resource
from boto3.dynamodb.conditions import Key, Attr

class Board:
    region = 'us-east-1'
    dynamodb = resource('dynamodb', region_name=region)
    table = dynamodb.Table('Board')

    def get_board(self):
        response = self.table.get_item(
            Key={
                'Board_ID': 1,
                'Sprint_ID': 123
            }
        )
        print(response)
        return response["Item"]


      

