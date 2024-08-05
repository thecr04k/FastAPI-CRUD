from fastapi import APIRouter


router = APIRouter()

@router.get(
    path        ="/",
    name        ="<sample title here>",
    description ="<sample description here>"
)
async def index():
    return {
        "Current Page": "Index"
    }