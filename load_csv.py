import sqlite3
import pandas as pd

DB_PATH = "grocery_data.db"

#defining a db path - DB_path and getting both the csv file into same DB 
def load_csv_to_sqlite():
    conn = sqlite3.connect(DB_PATH)

    # Load grocery_data into  'report'
    df1 = pd.read_excel("grocery_data.xlsx")
    df1.to_sql("report", conn, if_exists="replace", index=False)

    
    conn.close()
    print("✅ CSVs loaded into database.")

if __name__ == "__main__":
    load_csv_to_sqlite()