from fastapi import UploadFile
from ..services.recognition_service import RecognitionService


class RecognitionController:

    def __init__(self, recognition_service: RecognitionService) -> None:
        self.recognition_service = recognition_service

    async def verify(self, image: UploadFile) -> dict:
        return await self.recognition_service.verify(image)
