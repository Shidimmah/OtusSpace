from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Notification(BaseModel):
    user_id: str
    message: str

@app.post("/send-notification")
def send_notification(notification: Notification):
    print(f"Sending notification to user {notification.user_id}: {notification.message}")
    return {"message": "Notification sent successfully"}