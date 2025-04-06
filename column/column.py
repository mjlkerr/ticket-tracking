from boto3 import resource
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime

region = 'us-east-1'
dynamodb = resource('dynamodb', region_name=region)
table = dynamodb.Table('Board')

response = table.query(
    KeyConditionExpression=Key('Board_ID').eq('1')
)
items = response['Items']
print(items)