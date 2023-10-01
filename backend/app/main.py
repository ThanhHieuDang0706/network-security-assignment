from fastapi import FastAPI
from .routers import ciphers
from .constants import APP_TITLE
import uvicorn

""" write code to test here """

app = FastAPI(
    title=APP_TITLE,
)

app.include_router(
    ciphers.router
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)