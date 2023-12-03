from fastapi import FastAPI
from .routers import ciphers
from .constants import APP_TITLE
from .core.english_dict import ENGLISH_DICTIONARY
from fastapi.middleware.cors import CORSMiddleware
from os import getenv
""" write code to test here """

app = FastAPI(
    title=APP_TITLE,
)

app.include_router(
    ciphers.router
)

@app.on_event("startup")
async def load_dictionary():
    with open("./resources/english_dictionary.txt") as f:
        for line in f:
            global ENGLISH_DICTIONARY
            ENGLISH_DICTIONARY[line.strip()] = True

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/", tags="Root")
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

if __name__ == "__main__":
    import uvicorn
    port=int(getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port, reload=True)