from fastapi import APIRouter

router = APIRouter()

@router.get("/suppliers")
async def get_suppliers():
    return {"message": "List of suppliers"}
