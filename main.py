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