from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

replays_db = {}

class Replay(BaseModel):
    id: str
    game_id: str
    data: dict

@app.post("/save-replay")
def save_replay(replay: Replay):
    replays_db[replay.id] = replay
    return {"message": "Replay saved successfully"}

@app.get("/replay/{replay_id}")
def get_replay(replay_id: str):
    if replay_id not in replays_db:
        raise HTTPException(status_code=404, detail="Replay not found")
    return replays_db[replay_id]