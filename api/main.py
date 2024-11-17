from posix import error
from fastapi import FastAPI
import mysql.connector as msql
import dotenv
import os

dotenv.load_dotenv()

env_type = os.getenv("RUN_ENV")

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

user = os.getenv("DB_USER")
if user is None:
    error("No DB_USER environment variable found!")
    exit(1)

password = os.getenv("DB_PASSWORD")
if password is None:
    error("No DB_PASSWORD environment variable found!")
    exit(1)

db = msql.connect(
    user=user,
    password=password,
    host="localhost",
    database="Discreta"
)


@app.get("/api/hello")
def hello():
    return {"Hello": "World"}
