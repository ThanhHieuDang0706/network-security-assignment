from fastapi import FastAPI
from .routers import ciphers
from .constants import APP_TITLE
from .core.english_dict import ENGLISH_DICTIONARY
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)