from fastapi import FastAPI

from src.api import register_routes
from src.logging import configure_logging, LogLevels

configure_logging(LogLevels.info)

app = FastAPI()

register_routes(app)
