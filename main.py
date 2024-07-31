from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get(
    path="/",
    name= "FastAPI Index",
    description="Index of FastAPI"
)
async def index():
    return "HELLO"

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port= 14369)