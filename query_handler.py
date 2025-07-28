import pandas as pd
from analysis import expiry_loss_analysis, all_time_profit_analysis,add_order_placement_date

def process_user_query(user_input: str, sql: str, df: pd.DataFrame):
    """
    Routes analysis based on keywords and reuses pre-fetched DataFrame
    """
    user_input = user_input.lower()

    if all(k in user_input for k in ["loss", "expiry", "due to"]):
        return expiry_loss_analysis(df)

    elif all(k in user_input for k in [
    "what is lifetime revenue", 
    "what is all time revenue",
    "maximum revenue possible"
    ]):
        return all_time_profit_analysis(df)
    
    elif any(phrase in user_input for phrase in [
    "reorder placement date",
    "when to reorder",
    "when should i reorder",
    "reorder date",
    "restock date",
    "when should sku be restocked",
    "when to place order"
    ]):
        return add_order_placement_date(df)

    return None
