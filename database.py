import sqlite3

def init_db():
    conn = sqlite3.connect("parcel_tracker.db")
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS delivery_agents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS parcels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        receiver TEXT,
        address TEXT,
        status TEXT DEFAULT 'Pending',
        agent_id INTEGER,
        FOREIGN KEY(agent_id) REFERENCES delivery_agents(id)
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS tracking_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        parcel_id INTEGER,
        status TEXT,
        updated_on TEXT,
        FOREIGN KEY(parcel_id) REFERENCES parcels(id)
    )
    ''')

    conn.commit()
    conn.close()
