from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
async def health():
    return {"message": "alive!"}


@app.get("/")
async def read_root():
    return {"message": "Send your message!"}
