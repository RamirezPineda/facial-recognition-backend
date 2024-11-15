from fastapi import APIRouter, UploadFile
from ..services.recognition_service import RecognitionService
from ..controllers.recognition_controller import RecognitionController

router = APIRouter(tags=["Facial Recognition"])

recognition_service = RecognitionService()
recognition_controller = RecognitionController(recognition_service)


@router.post("/facial-recognition")
async def facial_recognition(image: UploadFile):
    return await recognition_controller.verify(image)
