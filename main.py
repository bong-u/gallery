import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return 'hello fastapi'

if __name__ == '__main__':
    uvicorn.run(app, port=80)