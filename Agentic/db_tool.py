import sqlite3
from pydantic_ai import Agent, RunContext

DB_PATH = "mobile_store.db"

def run_sql(ctx: RunContext, sql: str) -> list[dict]:
    """Execute SQL query"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    columns = [col[0] for col in cur.description] if cur.description else []
    result = [dict(zip(columns, row)) for row in rows]
    conn.close()
    return result