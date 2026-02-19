from typing import Optional
from fastapi import FastAPI,HTTPException,Response, status,Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg
from psycopg.rows import dict_row
import time
from sqlalchemy.orm import Session
from . import models
from .database import engine,get_db

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
class Post(BaseModel):
    title : str
    content: str
    published: bool = True

    
    
my_posts=[{"title": "who is the GOAT", "content":"Neymar is", "id": 1}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
def find_index(id):
    for i, p in enumerate(my_posts):
        if p["id"]==id:
            return i
        
        
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    # with conn.cursor() as cursor:
        # cursor.execute(""" SELECT * FROM posts""")
        # posts= cursor.fetchall()
        posts=db.query(models.Post).all()
        return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post : Post):
    print(post)
    cursor.execute(
        """
        INSERT INTO posts (title, content, published)
        VALUES (%s, %s, %s)
        RETURNING *
        """,
        (post.title, post.content, post.published)
    )

    new_post= cursor.fetchone()
    conn.commit()
    return {"data":new_post}


@app.get("/posts/{id}")
def get_post(id : int):
    cursor.execute("SELECT * FROM posts WHERE id = %s",(str(id,)))
    post= cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the post with {id} does not exist")
   
    return {"post details": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_postS(id:int):
    cursor.execute("""DELETE FROM posts WHERE id= %s RETURNING * """, (str(id),))
    deleted_post=cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post  with id : {id} does not exist")
   
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post:Post):
    cursor.execute("""UPDATE posts  SET title=%s, content=%s, published= %s WHERE id =%s RETURNING *""",(post.title,post.content,post.published,str(id)))
    updated_post=cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post  with id : {id} does not exist")
    
    
    return {"data": updated_post}



