from fastapi import APIRouter

router = APIRouter(
    prefix="/login",
    tags=["login"]
)

@router.get("/")
def hello_login():
    return {"hello": "login"}