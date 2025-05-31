from pydantic import BaseModel

class EmailText(BaseModel):
    email: str
