from uuid import uuid4

import uvicorn
from fastapi import FastAPI
from time import sleep
import os
from loguru import logger

app = FastAPI()


@app.get("/health")
def health():
    return "Ok"


@app.get("/load")
async def run_load_test():
    request_id = str(uuid4())
    logger.info(f"Starting request {request_id}")
    sleep(2)
    logger.info(f"Finished request {request_id}")
    return "Ok"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 6000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, log_level="debug")
