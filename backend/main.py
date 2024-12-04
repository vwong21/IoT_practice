from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from database import SessionLocal
from models import Device
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class DeviceCreate(BaseModel):
    name: str
    type: str
    uid: str

@app.get("/devices/")
async def get_devices(db: Session = Depends(get_db)):
    return db.query(Device).all()
    
@app.get("/devices/{id}")
async def get_device(id: int, db: Session = Depends(get_db)):
    device =  db.query(Device).filter(Device.id == id).first()
    if device is None:
        raise HTTPException(status_code=400, detail="Device not found")
    return device

@app.post("/devices/")
async def post_devices(device: DeviceCreate, db: Session = Depends(get_db)):
    new_device = Device(name=device.name, type=device.type, uid=device.uid)
    db.add(new_device)
    db.commit()
    db.refresh(new_device)
    return {"id": new_device.id, "name": new_device.name, "type": new_device.type, "uid": new_device.uid}

