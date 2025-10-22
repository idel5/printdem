from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import settings
from app.api.v1.routers import api_router
from app.db.session import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handles application startup and shutdown events.
    Startup: Initializes the database and creates tables.
    Shutdown: Placeholder for cleanup (e.g., closing resource pools).
    """
    # STARTUP LOGIC
    print("Initializing database...")
    # This runs the table creation upon startup
    await init_db() 
    print("Database ready.")
    
    # Yield control back to FastAPI to start serving requests
    yield

    # SHUTDOWN LOGIC (Placeholder)
    print("Shutting down resources...")
    # Add any necessary cleanup here (e.g., disconnecting from external services)


# --- Initialization ---
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan # <--- Use the new lifespan function here
)

# --- Include Routers ---
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": "Welcome to PrintDem API. Access documentation at /docs"}
