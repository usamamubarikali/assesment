from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from .models.response_model import ResponseModel
from .evaluation import get_recommendations
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

origins = [ 
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

allowed_seasons = ["summer", "winter", "autumn", "spring"]

@app.get("/recommendations", tags=["Dates"], status_code=status.HTTP_200_OK, response_model=ResponseModel)
def get_day_of_week(country: str, season: str):
    
    if season.lower() not in allowed_seasons:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Requested season is not valid")
    
    data = {
        "country": country,
        "season": season,
        "recommendations": get_recommendations(country=country, season=season)
    }

    return ResponseModel(**data)

