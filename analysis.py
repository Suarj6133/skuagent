import sqlite3
import pandas as pd
from datetime import datetime

today = pd.to_datetime(datetime.today().date())
DB_PATH = "grocery_data.db"


#1. expiry loss period
def expiry_loss_analysis(df: pd.DataFrame) -> pd.DataFrame:
    # Ensure correct types
    df['expiry_date'] = pd.to_datetime(df['expiry_date'], errors='coerce')
    df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')

    # Drop rows with invalid expiry dates
    df = df.dropna(subset=['expiry_date'])

    def calculate_leftover(row):
        count_of_days = (row['expiry_date'] - today).days
        expected_sales = count_of_days * row['daily_order_qty']
        left_over = row['Inventory'] - expected_sales
        return left_over if left_over >= 0 else 0

    def calculate_loss(row):
        count_of_days = (row['expiry_date'] - today).days
        expected_sales = count_of_days * row['daily_order_qty']
        left_over = row['Inventory'] - expected_sales
        if left_over <= 0:
            return 0
        return left_over * row['unit_price']

    # Apply both calculations
    df['left_over'] = df.apply(calculate_leftover, axis=1)
    df['loss_expected'] = df.apply(calculate_loss, axis=1)

    df = df.drop(columns=[
        "expiry_date", "reorder_time", "safety_stock"
    ])


    return df



#2.all time profit
def all_time_profit_analysis(df: pd.DataFrame) -> pd.DataFrame:
    # Ensure correct types
    df['expiry_date'] = pd.to_datetime(df['expiry_date'], errors='coerce')
    df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')

    # Drop rows with invalid expiry dates
    df = df.dropna(subset=['expiry_date'])


    def all_time_sale_value(row):
        count_of_days = (row['expiry_date'] - today).days
        expected_sales = count_of_days * row['daily_order_qty']
        return expected_sales * row['unit_price']

    # Apply both calculations
    df['life_time_profit'] = df.apply(all_time_sale_value, axis=1)
    return df

#3.orderplacement date
def add_order_placement_date(df: pd.DataFrame) -> pd.DataFrame:

    def compute_order_date(row):
        try:
            if row['daily_order_qty'] == 0:
                return None

            expected_closing_days = round(row['Inventory'] / row['daily_order_qty'], 0)
            order_day_offset = expected_closing_days - row['reorder_time']

            # Compute order date
            order_date = today + pd.Timedelta(days=order_day_offset)
            return order_date.date()
        except Exception as e:
            return None  # In case of missing or bad values

    df['orderplacement_date'] = df.apply(compute_order_date, axis=1)
    df = df.drop(columns=[
        "expiry_date", "reorder_time", "safety_stock"
    ])
    return df
