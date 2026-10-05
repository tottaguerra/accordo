from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pathlib import Path
import os
from sqlalchemy import create_engine, text

# Carregar variáveis de ambiente (especificar caminho)
env_path = Path(__file__).parent / '.env'
load_dotenv(env_path)
DATABASE_URL = os.getenv("DATABASE_URL")

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://192.168.15.4:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check
@app.get("/api/health")
def health():
    return {"status": "ok"}

# Test database connection
@app.get("/api/db/test")
def test_db():
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            return {"status": "ok", "db_connected": True}
    except Exception as e:
        return {"status": "error", "message": str(e)}
