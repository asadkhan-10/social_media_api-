from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings  # import your Pydantic settings

# Build the DATABASE_URL from Pydantic settings
DATABASE_URL = (
    f"postgresql://{settings.database_username}:"
    f"{settings.database_password}@"
    f"{settings.database_hostname}:"
    f"{settings.database_port}/"
    f"{settings.database_name}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


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
