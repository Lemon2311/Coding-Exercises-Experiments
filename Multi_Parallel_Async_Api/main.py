from fastapi import FastAPI, Body
from databases import Database
from sqlalchemy import MetaData, Table, create_engine, text

import asyncio

import sqlite3

app = FastAPI()

db_url="mysql+asyncmy://root:marcusor1@localhost:3306/"

databse = Database(db_url)

@app.add_event_handler("startup")
async def startup():
    await databse.connect()





#@app.get("/get")
#async def get_thing():
 #   return {"thing": thing}

#@app.put("/put")
#async def put_thing(new_thing: str = Body(...)):
 #   global thing
  #  thing = new_thing
   # return {"thing": thing}