from boto3 import resource
from boto3.dynamodb.conditions import Key, Attr

region = 'us-east-1'
dynamodb = resource('dynamodb', region_name=region)
table = dynamodb.Table('Board')

def get_columns():
    response = table.scan(AttributesToGet=['Columns'])
    print(response["Items"])
    return response["Items"]
get_columns()
