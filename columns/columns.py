from boto3 import resource
from boto3.dynamodb.conditions import Key, Attr

region = 'us-east-1'
dynamodb = resource('dynamodb', region_name=region)
table = dynamodb.Table('Board')

def get_columns():
    response = table.scan(AttributesToGet=['Status_Columns'])
    print(response["Items"])
    return response["Items"]
get_columns()

def rename_status_columns(old_name, new_name):
    """
    Rename a status column in the DynamoDB table.
    """
    response = table.scan(AttributesToGet=['Status_Columns'])
    status_columns = response["Items"][0]["Status_Columns"]
    # Check if the old name exists
    for status in status_columns:
        if old_name == status:
            status_columns[status_columns.index(old_name)] = new_name
            break
    else:
        raise HTTPException(status_code=404, detail=f"Status column '{old_name}' does not exist.")
    # Update the item in the DynamoDB table
    response = table.update_item(
        Key={
            'Board_ID': 1,
            'Sprint_ID': 123
        },
        UpdateExpression="SET Status_Columns = :val",
        ExpressionAttributeValues={
            ':val': status_columns
        }
    )
    return response
