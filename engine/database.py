import sqlite3

def init_db():
    conn = sqlite3.connect("greenops.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS deployments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        region TEXT,
        carbon INTEGER,
        green_score REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def insert_deployment(region, carbon, score):
    conn = sqlite3.connect("greenops.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO deployments (region, carbon, green_score)
    VALUES (?, ?, ?)
    """, (region, carbon, score))

    conn.commit()
    conn.close()


def get_deployments():
    conn = sqlite3.connect("greenops.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM deployments ORDER BY timestamp DESC")
    rows = cursor.fetchall()

    conn.close()
    return rows
