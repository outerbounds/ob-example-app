import os
import json
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"model": model}


if __name__ == "__main__":
    try:
        with open(os.path.join(os.path.dirname(__file__), "data.json")) as f:
            model = json.load(f)["model"]
        print("model loaded!")
    except:
        print("no model")
        model = "[no model found]"
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=6000)
