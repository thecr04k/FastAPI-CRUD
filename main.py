from fastapi import FastAPI, HTTPException
import uvicorn


app = FastAPI()


@app.get(
    path="/",
    name= "FastAPI Index",
    description="Index of FastAPI"
)
async def index():
    return {
        "Index":{
            "Title"     :"CRUD By John Edward Capellan using FastAPI",
            "Message"   :"Welcome to the Index page of my Sample CRUD that uses FastAPI Framework and MongoDB as my Database",
            "Tools_used":[
                "FastAPI",
                "MongoDB",
                "Python"    
            ]
        }
    }



if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port= 14369, reload=True)