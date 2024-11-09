# api/main.py
import os
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
import psycopg2
from psycopg2.extras import Json
from secrets import token_hex
import numpy as np

app = FastAPI()
api_key_header = APIKeyHeader(name="X-API-Key")

def get_db_connection():
    return psycopg2.connect(
        host="postgres",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )

def verify_api_key(api_key: str = Depends(api_key_header)):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT api_key FROM api_keys WHERE api_key = %s", (api_key,))
    if cursor.fetchone() is None:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    conn.close()

@app.post("/insert_vector")
async def insert_vector(description: str, embedding: list[float], api_key: str = Depends(verify_api_key)):
    if len(embedding) != 1536:
        raise HTTPException(status_code=400, detail="Embedding must be 1536 dimensions")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (description, embedding) VALUES (%s, %s) RETURNING id",
        (description, Json(embedding))
    )
    item_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return {"id": item_id, "description": description}

@app.get("/similar_items")
async def get_similar_items(query_vector: list[float], api_key: str = Depends(verify_api_key)):
    if len(query_vector) != 1536:
        raise HTTPException(status_code=400, detail="Query vector must be 1536 dimensions")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, description FROM items ORDER BY embedding <-> %s LIMIT 5",
        (Json(query_vector),)
    )
    results = cursor.fetchall()
    conn.close()
    return {"similar_items": [{"id": r[0], "description": r[1]} for r in results]}

@app.post("/generate_api_key")
async def generate_api_key(description: str):
    api_key = token_hex(32)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO api_keys (api_key, description) VALUES (%s, %s) RETURNING api_key",
        (api_key, description)
    )
    conn.commit()
    conn.close()
    return {"api_key": api_key, "description": description}
