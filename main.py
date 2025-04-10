from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from board import Board
from boto3 import resource
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse



app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/getBoard")
def get_board():
    """
    Get the board information from the DynamoDB table.
    We only have one board to keep it simple.
    """
    response = Board.table.get_item(
        Key={
            'Board_ID': 1,
            'Sprint_ID': 123
        }
    )
    
    # Check if the item exists
    if 'Item' not in response:
        raise HTTPException(status_code=404, detail="Board not found")
    return response["Item"]

@app.get("/getTickets")
def get_tickets():
    """
    Get the tickets from the DynamoDB table.
    """
    response = Board.table.scan(AttributesToGet=['Tickets'])
    
    # Check if the item exists
    if 'Items' not in response:
        raise HTTPException(status_code=404, detail="Tickets not found")
    
    return response["Items"]

@app.get("/getstatusColumns")
def get_Status_Columns():
    """
    Get the Status_Columns from the DynamoDB table.
    """
    response = Board.table.scan(AttributesToGet=['Status_Columns'])
    print(response)
    
    # Check if the item exists
    if 'Items' not in response:
        raise HTTPException(status_code=404, detail="Status_Columns not found")
    
    return response["Items"]

@app.get("/getTicketsByColumn/")
def get_tickets_by_column(column: str):
    """
    Get the tickets by column from the DynamoDB table.
    """
    tickets = Board.table.scan(AttributesToGet=['Tickets'])
    print('tickets', tickets["Items"])
    response = tickets["Items"](
        FilterExpression=Attr('Column').eq(column),
    )
    print('response', response)
    
    # Check if the item exists
    if 'Items' not in response:
        raise HTTPException(status_code=404, detail="Tickets not found")
    
    return response["Items"]

@app.post("/renameStatusColumn")
def rename_status_column(old_name: str, new_name: str):
    """
    Rename a status column in the DynamoDB table.
    """
    response = Board.table.scan(AttributesToGet=['Status_Columns'])
    status_columns = response["Items"][0]["Status_Columns"]
    # Check if the old name exists
    for item in status_columns:
        if old_name == item['Name']:
            item['Name'] = new_name
            break
    else:
        raise HTTPException(status_code=404, detail=f"Status column '{old_name}' does not exist.")
    
    # Update the item in the DynamoDB table
    response = Board.table.update_item(
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




