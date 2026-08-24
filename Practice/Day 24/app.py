from fastapi import FastAPI
from pydantic import BaseModel
import logging

from config import APP_NAME, APP_VERSION, ENVIRONMENT, LOG_LEVEL
# Create FastAPI application
app = FastAPI(
    title=APP_NAME,
    description="Production-ready company support API",
    version=APP_VERSION
)

# Logging configuration
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="a"
)

logger = logging.getLogger(__name__)


# Request model
class SupportRequest(BaseModel):
    name: str
    message: str


# Home API
@app.get("/")
def home():
    logger.info("Home endpoint accessed")
    return {
        "status": "success",
        "message": "Company Support API is running"
    }


# Health check API
@app.get("/health")
def health_check():
    logger.info("Health check performed")
    return {
        "status": "healthy"
    }


# Company information API
@app.get("/company")
def company_info():
    logger.info("Company information requested")
    return {
        "company": "ABC Technologies",
        "service": "Customer Support",
        "status": "active"
    }


# Support request API
@app.post("/support")
def create_support_request(request: SupportRequest):
    logger.info(
        f"Support request received from {request.name}"
    )

    return {
        "status": "success",
        "message": "Support request received",
        "customer": request.name
    }