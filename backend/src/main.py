from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config.database import SessionLocal, engine
from .lifespan import database_lifespan
from src.models import feedback as models
from src.routers import feedback as feedback_router
from src.auth import routes
from src.config.config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME, lifespan=database_lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# router connections
app.include_router(feedback_router.router)
app.include_router(routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Feedback API!"}
