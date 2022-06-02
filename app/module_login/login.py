from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def hello_login(a: str):
    return { a : "login"}
