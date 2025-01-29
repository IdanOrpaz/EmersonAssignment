from fastapi import FastAPI
from routes.analyze_router import router as analyze_router
from routes.start_router import router as start_router

# Create the main FastAPI app
app = FastAPI()

# Include the analyze router
app.include_router(analyze_router)
app.include_router(start_router)

