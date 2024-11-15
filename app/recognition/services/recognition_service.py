import base64
from deepface import DeepFace
from fastapi import UploadFile, HTTPException


class RecognitionService:
    def __init__(self) -> None:
        pass

    async def verify(self, image: UploadFile) -> dict:

        if image.content_type not in ["image/jpeg", "image/jpg", "image/png"]:
            raise HTTPException(
                status_code=400, detail="Only JPEG, JPG or PNG images are accepted"
            )

        image_contents = await image.read()
        encoded_image = base64.b64encode(image_contents).decode("utf-8")
        image_data_uri = (
            f"data:image/{image.content_type.split('/')[1]};base64,{
                encoded_image}"
        )
        result = DeepFace.verify(
            img1_path=image_data_uri,
            img2_path="./assets/img2.jpg",
        )

        return {"filename": image.filename, "result": result}
