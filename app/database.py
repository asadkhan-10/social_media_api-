import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# for working with raw sql

# while True:
#     try:
#         conn = psycopg.connect(
#         dbname="fastapi",
#         user="postgres",
#         password="",
#         host="localhost",
#         row_factory=dict_row)
#         cursor= conn.cursor()

#         print("Database connection successful")
#         break
#     except Exception as error:
#         print("connection failed")
#         print("Error is ", error)
#         time.sleep(2)
