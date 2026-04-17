from fastapi import FastAPI

app = FastAPI()

current_state = {
    "position": [0, 0],
    "motion": "stationary"
}

@app.get("/state")
def get_state():
    return current_state

@app.post("/update")
def update_state(data: dict):
    global current_state
    current_state = data
    return {"status": "updated"}