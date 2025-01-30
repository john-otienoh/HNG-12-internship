from datetime import datetime, timezone
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BasicInfo(BaseModel):
    """Model for the response"""
    email: str
    current_datetime: str
    github_url: str

my_info = {
    "email": "johnteclaire@gmail.com",
    "current_datetime": "",
    "github_url": "https://github.com/john-otienoh/HNG12_Internship"    
}

@app.get("/info", response_model=BasicInfo)
async def get_my_info():
    "Retreive Basic information"

    my_info["current_datetime"] = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    return my_info
