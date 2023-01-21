from uuid import uuid4

from flask import Flask
from time import sleep
import os

from loguru import logger

app = Flask(__name__)


@app.route("/health")
def health():
    return "Ok"


@app.route("/load")
def run_load_test():
    request_id = str(uuid4())
    logger.info(f"Starting request {request_id}")
    sleep(2)
    logger.info(f"Finished request {request_id}")
    return "Ok"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 6000))
    app.run(debug=True, host='0.0.0.0', port=port)
