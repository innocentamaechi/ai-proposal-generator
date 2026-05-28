from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config.config import settings
from app.config.logging_config import get_logger

from app.database.db import Base
from app.database.db import engine

from app.routes.api import router as api_router
from app.routes.web import router as web_router

from app.database import models


models.Base.metadata.create_all(bind=engine)

logger = get_logger()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

app.include_router(api_router)
app.include_router(web_router)


@app.on_event("startup")
async def startup_event():

    logger.info("Application started successfully")
