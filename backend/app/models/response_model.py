from pydantic import BaseModel

class ResponseModel(BaseModel):
    country: str
    season: str
    recommendations: list