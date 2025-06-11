from src.generate_interests import process_persona_and_update

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/process-persona/")
def process_persona(persona_input: dict):
    try:
        persona_data = persona_input
        updated_persona = process_persona_and_update(persona_data)
        return {"status": "success", "data": updated_persona}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
