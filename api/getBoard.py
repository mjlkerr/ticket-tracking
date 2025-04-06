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
@app.get("/getBoard")
def read_root():
    return {"Hello": "World"}