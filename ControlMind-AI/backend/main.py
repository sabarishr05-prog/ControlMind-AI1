from fastapi import FastAPI
from routes.sensor import router as sensor_router
from routes.plc import router as plc_router
from routes.pid import router as pid_router
from routes.datasheet import router as datasheet_router
from routes.arduino import router as arduino_router
from routes.troubleshooting import router as trouble_router

app = FastAPI(
    title="ControlMind AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to ControlMind AI"
    }

app.include_router(sensor_router)
app.include_router(plc_router)
app.include_router(pid_router)
app.include_router(datasheet_router)
app.include_router(arduino_router)
app.include_router(trouble_router)