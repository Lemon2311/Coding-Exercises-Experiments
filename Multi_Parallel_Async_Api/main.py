from fastapi import FastAPI, Body
import asyncio

app = FastAPI()

thing = "hello world"

@app.get("/get")
async def get_thing():
    return {"thing": thing}

@app.put("/put")
async def put_thing(new_thing: str = Body(...)):
    global thing
    thing = new_thing
    return {"thing": thing}