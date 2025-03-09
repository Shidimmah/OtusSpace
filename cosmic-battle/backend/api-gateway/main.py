from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

SERVICES = {
    "user": "http://user-service:8000",
    "game": "http://game-service:8001",
    "tournament": "http://tournament-service:8002",
    "notification": "http://notification-service:8003",
    "agent": "http://agent-service:8004",
    "replay": "http://replay-service:8005",
    "rating": "http://rating-service:8006",
}

@app.post("/{service}/{endpoint}")
async def proxy_request(service: str, endpoint: str, data: dict):
    if service not in SERVICES:
        raise HTTPException(status_code=404, detail="Service not found")
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{SERVICES[service]}/{endpoint}", json=data)
        return response.json()