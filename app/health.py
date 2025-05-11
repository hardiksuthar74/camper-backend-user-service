from fastapi import APIRouter
from sqlalchemy import text
from core.db.session import session

api_router = APIRouter()


@api_router.get("/health")
async def health():
    """
    Health check endpoint.
    """
    await session.execute(text("SELECT 1"))
    return {"status": "healthy"}
