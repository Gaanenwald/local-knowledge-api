from main import app


@app.get("/health")
async def health():
    return {"status": "ok"}