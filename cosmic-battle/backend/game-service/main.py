from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

games_db = {}

class Game(BaseModel):
    id: str
    status: str
    participants: List[str]

@app.post("/create-game")
def create_game(game: Game):
    games_db[game.id] = game
    return {"message": "Game created successfully", "game_id": game.id}

@app.get("/game/{game_id}")
def get_game(game_id: str):
    if game_id not in games_db:
        raise HTTPException(status_code=404, detail="Game not found")
    return games_db[game_id]