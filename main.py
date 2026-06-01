from fastapi import FastAPI
from routes import router

app = FastAPI(title="Address API")
app.include_router(router)
