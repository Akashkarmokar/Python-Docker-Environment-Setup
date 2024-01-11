from fastapi import FastAPI

app = FastAPI()


import debugpy
debugpy.listen(("0.0.0.0", 5678))

@app.get("/")
async def root():
    return {"message": "Hello World."}
