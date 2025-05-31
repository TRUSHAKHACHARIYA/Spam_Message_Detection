from fastapi import APIRouter, HTTPException
from app.schema import EmailText
from app.core.model_handler import ModelHandler

router = APIRouter()
model_handler = ModelHandler()

@router.post("/predict")
async def predict_spam(email_text: EmailText):
    if not email_text.email.strip():
        raise HTTPException(status_code=400, detail="Email text is empty")
    prediction = model_handler.predict(email_text.email)
    return {"prediction": prediction}
