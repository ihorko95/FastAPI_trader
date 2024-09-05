from enum import Enum
from fastapi import FastAPI
import  uvicorn
app=FastAPI()

class ModelName(str,Enum):
    alex='alex'
    olga='olga'
    rone='rone'

@app.get('/')
async def hello():
    return 'Fast API project for traders.'

@app.get('/user/{user_name}')
async def user(user_name:ModelName):
    return {'user_name':user_name}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
def main():
    print('Fast API project for traders.')

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, log_level="debug")
