import sqlite3
import pandas as pd

def run_sql_query(db_path, query):
    conn = sqlite3.connect(db_path)
    try:
        df = pd.read_sql_query(query, conn)
        return df
    finally:
        conn.close()