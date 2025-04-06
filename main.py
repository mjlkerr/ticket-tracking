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

@app.get("/getColumns")
def get_columns():
    """
    Get the columns from the DynamoDB table.
    """
    response = Board.table.scan(AttributesToGet=['Columns'])
    print(response)
    
    # Check if the item exists
    if 'Items' not in response:
        raise HTTPException(status_code=404, detail="Columns not found")
    
    return response["Items"]


