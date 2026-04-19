import uvicorn
import logging
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

logging.getLogger("uvicorn.access").disabled = True
logging.getLogger("uvicorn.error").disabled = True

app = FastAPI()

@app.get("/plaintext", response_class=PlainTextResponse)
def plaintext():
    return "Hello, World!"

@app.get("/json")
def json_endpoint():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
		uvicorn.run(app, host="0.0.0.0", port=5000, workers=1, log_config=None)