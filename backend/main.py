# backend/main.py
# This is the entry point of our FastAPI backend
# Railway will run this file

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create the FastAPI application
app = FastAPI(
    title="DSRT CEOS API",
    description="Construction Enterprise Operating System - Backend",
    version="1.0.0"
)

# CORS = Allow frontend to talk to backend
# Without this, browser blocks the connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",           # Your laptop frontend
        "https://*.vercel.app",            # Vercel frontend
        "*"                                # Allow all for now
    ],
    allow_credentials=True,
    allow_methods=["*"],                   # Allow GET, POST, PUT, DELETE
    allow_headers=["*"],                   # Allow all headers
)

# TEST ROUTE 1: Root
# When someone visits: https://yourapp.railway.app/
@app.get("/")
def root():
    return {
        "message": "DSRT CEOS API is running!",
        "version": "1.0.0",
        "status": "healthy"
    }

# TEST ROUTE 2: Health Check
# Railway uses this to check if app is alive
# When someone visits: https://yourapp.railway.app/health
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "DSRT CEOS Backend"
    }

# TEST ROUTE 3: Test API
# When someone visits: https://yourapp.railway.app/api/v1/test
@app.get("/api/v1/test")
def test():
    return {
        "message": "API is working!",
        "data": {
            "company": "DSRT CEOS",
            "module": "Test"
        }
    }