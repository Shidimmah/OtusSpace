from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

agents_db = {}

class Agent(BaseModel):
    id: str
    user_id: str
    code: str

@app.post("/register-agent")
def register_agent(agent: Agent):
    agents_db[agent.id] = agent
    return {"message": "Agent registered successfully"}

@app.get("/agent/{agent_id}")
def get_agent(agent_id: str):
    if agent_id not in agents_db:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agents_db[agent_id]