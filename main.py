from fastapi import FastAPI
from . import OrganizerAPI, TaskAPI

app = FastAPI()

app.include_router(OrganizerAPI.router)
app.include_router(TaskAPI.router)