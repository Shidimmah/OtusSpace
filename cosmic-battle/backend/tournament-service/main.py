from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

tournaments_db = {}

class Tournament(BaseModel):
    id: str
    name: str
    status: str
    participants: List[str]

@app.post("/create-tournament")
def create_tournament(tournament: Tournament):
    tournaments_db[tournament.id] = tournament
    return {"message": "Tournament created successfully", "tournament_id": tournament.id}

@app.get("/tournament/{tournament_id}")
def get_tournament(tournament_id: str):
    if tournament_id not in tournaments_db:
        raise HTTPException(status_code=404, detail="Tournament not found")
    return tournaments_db[tournament_id]