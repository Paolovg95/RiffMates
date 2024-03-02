# RiffMates/home/api.py
from ninja import Router

router = Router()

@router.get("/")
def home(request):
    return "RiffMates rocks!"

@router.get("/version/")
def version(request):
    data = {
        "version": "1.0.0",
        "stage": "development"
    }
    return data
