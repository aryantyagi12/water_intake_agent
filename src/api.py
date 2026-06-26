from fastapi import FastAPI
from pydantic import BaseModel
from src.agent import waterintake
from src.database import log_intake, get_intake
from src.logger import log_info,log_error

app=FastAPI()
agent=waterintake()

class intakeRequest(BaseModel):
    user_id:str
    intake_ml:int

@app.post("/log_intake")
async def log_water_intake(request:intakeRequest):
    
    log_intake(request.user_id,request.intake_ml)
    analysis=agent.analyse_intake(request.intake_ml)
    log_info(f"user {request.user_id} logged {request.intake_ml}ml")
    return {"message":"Intake logged successfully","analysis":analysis}
@app.get("/history/{user_id}")
async def get_water_history(user_id:str):
    history=get_intake(user_id)
    return {"user_id":user_id,"history":history}

