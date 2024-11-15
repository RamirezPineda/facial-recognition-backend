from fastapi import APIRouter

from recognition.routes import recognition_routes

router = APIRouter(prefix='/api')

router.include_router(recognition_routes.router)
