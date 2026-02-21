from typing import Optional
from fastapi import FastAPI,HTTPException,Response, status,Depends
from fastapi.params import Body
from random import randrange
import psycopg
from psycopg.rows import dict_row
import time
from sqlalchemy.orm import Session
from . import models,schemas,utils
from .database import engine,get_db
from .routers import post, user

models.Base.metadata.create_all(bind=engine)


while True:
    try:
        conn = psycopg.connect(
        dbname="fastapi",
        user="postgres",
        password="1234",
        host="localhost",
        row_factory=dict_row)
        cursor= conn.cursor()
        
        print("Database connection successful")
        break
    except Exception as error:
        print("connection failed")
        print("Error is ", error)
        time.sleep(2)

app= FastAPI()
app.include_router(post.router)
app.include_router(user.router) 
@app.get("/")
def root():
    return {"message": "Hello World"}

