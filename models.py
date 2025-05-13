import sqlite3
from datetime import datetime

class DeliveryAgent:
    def __init__(self, db="parcel_tracker.db"):
        self.db = db

    def add_agent(self, name):
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO delivery_agents (name) VALUES (?)", (name,))
            conn.commit()

    def list_agents(self):
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM delivery_agents")
            return cur.fetchall()


class Parcel:
    def __init__(self, db="parcel_tracker.db"):
        self.db = db

    def add_parcel(self, sender, receiver, address, agent_id):
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO parcels (sender, receiver, address, agent_id) VALUES (?, ?, ?, ?)",
                (sender, receiver, address, agent_id),
            )
            conn.commit()

    def update_status(self, parcel_id, new_status):
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("UPDATE parcels SET status=? WHERE id=?", (new_status, parcel_id))
            cur.execute("INSERT INTO tracking_log (parcel_id, status, updated_on) VALUES (?, ?, ?)",
                        (parcel_id, new_status, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            conn.commit()

    def track_parcel(self, parcel_id):
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM parcels WHERE id=?", (parcel_id,))
            return cur.fetchone()

    def show_logs(self, parcel_id):
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("SELECT status, updated_on FROM tracking_log WHERE parcel_id=?", (parcel_id,))
            return cur.fetchall()

    def list_all_parcels(self):
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM parcels")
            return cur.fetchall()
