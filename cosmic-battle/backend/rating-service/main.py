from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

ratings_db = {}

class Rating(BaseModel):
    user_id: str
    score: int

@app.post("/update-rating")
def update_rating(rating: Rating):
    ratings_db[rating.user_id] = rating
    return {"message": "Rating updated successfully"}

@app.get("/rating/{user_id}")
def get_rating(user_id: str):
    if user_id not in ratings_db:
        raise HTTPException(status_code=404, detail="Rating not found")
    return ratings_db[user_id]