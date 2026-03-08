from fastapi import FastAPI
from app.routes.articles import router as articles_router

app = FastAPI(title="ost-tok")

app.include_router(articles_router, prefix="/articles", tags=["articles"])


@app.get("/")
def root():
    return {"status": "ok", "service": "ost-tok"}