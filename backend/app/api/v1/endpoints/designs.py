from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_designs():
    return {"message": "Design endpoints placeholder."}
