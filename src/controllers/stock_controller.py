from fastapi import FastAPI

from src.repository.stock_repository import stock_repository

app = FastAPI()


@app.get("/stocks")
async def get_stocks():
    stock_repo = stock_repository(None)
    return stock_repo.get_all_stocks()
