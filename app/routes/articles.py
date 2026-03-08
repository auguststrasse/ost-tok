from fastapi import APIRouter
from pydantic import BaseModel
from app.services.script_generator import generate_tiktok_variants

router = APIRouter()


class ArticleInput(BaseModel):
    title: str
    body: str
    region: str | None = None


@router.post("/generate")
def generate_article_variants(article: ArticleInput):
    variants = generate_tiktok_variants(
        title=article.title,
        body=article.body,
        region=article.region or "Ostdeutschland",
    )

    return {"variants": variants}