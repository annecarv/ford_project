from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.db.session import Base, session
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = "prod"
DATABASE_URL = os.getenv("DATABASE_URL")

engine_temp = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/postgres",
    isolation_level="AUTOCOMMIT",
    echo=True
)

with engine_temp.connect() as connection:
    result = connection.execute(text(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'"))
    if not result.scalar():
        connection.execute(text(f"CREATE DATABASE {DB_NAME}"))
        print(f"DB '{DB_NAME}' criado.")
    else:
        print(f"DB '{DB_NAME}' já existe.")

engine = create_engine(
    DATABASE_URL,
    isolation_level="AUTOCOMMIT",
    echo=True
)


