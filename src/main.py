from fastapi import FastAPI
from routes.root import router as root_router
from configs.postgres import engine
from models.databasemodel import Base

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Register API routes
app.include_router(root_router)

