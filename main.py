import os
import sqlite3
from fastapi import FastAPI

app = FastAPI()

# Ensure the database path is accessible
db_path = os.path.join(os.getcwd(), "count.db")
conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS counter (id INTEGER PRIMARY KEY, count INTEGER)")
cursor.execute("INSERT OR IGNORE INTO counter (id, count) VALUES (1, 0)")
conn.commit()

@app.get("/count")
def get_count():
    cursor.execute("UPDATE counter SET count = count + 1 WHERE id = 1")
    conn.commit()
    cursor.execute("SELECT count FROM counter WHERE id = 1")
    count = cursor.fetchone()[0]
    return {"count": count}
