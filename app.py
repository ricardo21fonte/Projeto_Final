import os
from pathlib import Path

from fastapi import FastAPI

app = FastAPI(title="Support API - Trabalho Integrador")
COUNTER_FILE = Path(os.getenv("DATA_DIR", "/data")) / "visitas.txt"


def read_visits() -> int:
    if not COUNTER_FILE.exists():
        return 0
    return int(COUNTER_FILE.read_text(encoding="utf-8").strip())


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": os.getenv("SERVICE_NAME", "support-api"),
        "version": "1.0",
        "team": "support",
    }


@app.get("/visits")
def get_visits():
    return {"visits": read_visits()}


@app.post("/visits")
def increment_visits():
    COUNTER_FILE.parent.mkdir(parents=True, exist_ok=True)
    count = read_visits() + 1
    COUNTER_FILE.write_text(str(count), encoding="utf-8")
    return {"visits": count}
