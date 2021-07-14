from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.utils.log_util import LogFactory, logger_name
from src.apis import parking_lot_apis
from src.apis import rate_card_apis
from src.apis import parking_info_apis

import logging
import os


LogFactory.configure_logger(
    logger_name=logger_name, logging_level=os.environ.get("LOGGING_LEVEL", "WARNING")
)
logger = logging.getLogger(logger_name)

app = FastAPI(title="Parking App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(parking_lot_apis.parking_lot_router, tags=["Tag Version 1"])
app.include_router(rate_card_apis.rate_card_router, tags=["Tag Version 1"])
app.include_router(parking_info_apis.parking_info_router, tags=["Tag Version 1"])

@app.get("/")
def read_root():
    return {"version": "0.1", "name": "parking lot service received REST API"}


@app.get("/health")
def health():
    return {"status": "ok"}
