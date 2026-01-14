from fastapi import FastAPI

app = FastAPI(title="Cybersecurity Training Platform")

@app.get("/health")
async def health():
    return {"status": "ok"}