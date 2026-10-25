from contextlib import asynccontextmanager
from fastapi import FastAPI
from zerodha_mcp.first import loginKite


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Server is running"}
