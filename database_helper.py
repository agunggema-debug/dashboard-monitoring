import sqlite3
import pandas as pd

def init_db():
    """Membuat database dan tabel jika belum ada."""
    conn = sqlite3.connect('monitoring.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS system_status
                 (id INTEGER PRIMARY KEY AUTO_INCREMENT,
                  channel TEXT, 
                  uptime REAL, 
                  response_time INTEGER, 
                  status TEXT, 
                  transactions INTEGER,
                  last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def fetch_data_from_sql():
    """Mengambil data terbaru dari database untuk dashboard."""
    conn = sqlite3.connect('monitoring.db')
    # Mengambil data terbaru untuk setiap channel
    query = """
    SELECT channel, uptime, response_time, status, transactions 
    FROM system_status 
    WHERE id IN (SELECT MAX(id) FROM system_status GROUP BY channel)
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df