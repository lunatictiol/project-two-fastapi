from fastapi import FastAPI, Body

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}