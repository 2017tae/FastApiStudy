from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from database import engineconn
from models import Test

# from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# origins =["http://localhost:5173",]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#
# )

engine= engineconn()
session = engine.sessionmaker()

class Item(BaseModel):
    name: str
    number : int

@app.get("/hello")
def hello():
    return {"message": "안녕하세요"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port = 8000)