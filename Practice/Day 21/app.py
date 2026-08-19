from pydantic import BaseModel, Field
from fastapi import FastAPI, Request, BackgroundTasks, Depends
import asyncio
import time

app = FastAPI(
    title="Day 21 Async FastAPI",
    description="Internship Day 21 - Async Programming and Performance",
    version="1.0.0"
)


# Validation Model
class User(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(ge=18, le=100)
    email: str


# Middleware - Response Time Measurement
@app.middleware("http")
async def add_process_time(request: Request, call_next):
    start_time = time.perf_counter()

    response = await call_next(request)

    process_time = time.perf_counter() - start_time

    response.headers["X-Process-Time"] = f"{process_time:.6f}"

    return response


# Synchronous API
@app.get("/sync")
def sync_endpoint():
    time.sleep(0.1)

    return {
        "type": "synchronous",
        "message": "This is a synchronous API"
    }


# Asynchronous API
@app.get("/async")
async def async_endpoint():
    await asyncio.sleep(0.1)

    return {
        "type": "asynchronous",
        "message": "This is an asynchronous API"
    }


# Background Task
def save_log(message: str):
    with open("activity.log", "a") as file:
        file.write(message + "\n")


@app.post("/background-task")
async def background_task(
    message: str,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(save_log, message)

    return {
        "status": "success",
        "message": "Background task added successfully"
    }


# User Validation API
@app.post("/users")
async def create_user(user: User):
    return {
        "message": "User created successfully",
        "user": user
    }

def get_current_user():
    return {
        "username": "intern",
        "role": "developer"
    }

@app.get("/profile")
async def get_profile(current_user: dict = Depends(get_current_user)):
    return {
        "message": "Profile fetched successfully",
        "user": current_user
    }

# API Version 1
@app.get("/api/v1/info")
async def api_v1_info():
    return {
        "version": "1.0",
        "message": "Welcome to API Version 1"
    }


# API Version 2
@app.get("/api/v2/info")
async def api_v2_info():
    return {
        "version": "2.0",
        "message": "Welcome to API Version 2",
        "status": "active"
    }