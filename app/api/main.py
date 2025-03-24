from fastapi import FastAPI
from .routes import suppliers, transactions

app = FastAPI()

app.include_router(suppliers.router)
#app.include_router(transactions.router)
