from fastapi import FastAPI
from app.routers import word_router

app = FastAPI(
    title="Vocabulary Tracker API",
    version="1.0.0"
)

app.include_router(word_router.router)