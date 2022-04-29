from fastapi import FastAPI
import subprocess
app = FastAPI()


@app.get("/")
def hello_world():
    result = subprocess.call(["nvidia-smi"])
    return {"message": "result"}