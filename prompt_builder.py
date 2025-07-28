def build_prompt(user_input: str) -> str:
    return f"""

 The data is stored in a SQLite database with one tables. The data is about a grocery shops SKUs with other detials.

Table 1: report
Below are the column lables in report with their meanings:
- `SKU`: Unique Id of each of the item that is being sold from the shop (eg: SKU-1 to be always read as together)
- `Inventory`: Current stock available / Quantity available of the SKU in the shop
- `daily_order_qty`: This is expected sales quantity / unit for each day for each of the SKU 
- `expiry_date` : Beyond this date the SKU won't be fit for sell (format - YYYY-MM-DD)
- `unit_price`: Selling price of each of the SKUs per unit / quantity
- `re-order_time`: Time taken to refill the the SKU that time from new order placement for procurement to stock arrival in the shop.
- `safety_stock`: Indicates the safety level defined as: (re-order time * daily order quantity * 10% )
    

Use only valid SQLite syntax. Do NOT use INFORMATION_SCHEMA.

---

### Special Instructions:
- Always treat values in the `SKU` columns as exact string matches.Do not split them or apply partial matching unless explicitly asked.

- If the question is vague or unclear or doesn’t match any pattern, return:  
`SELECT * FROM report;

- If the user asks **lifetime revenue** or **all time revenue** or **maximum revenue possible**?
`SELECT *
  FROM report;`

- Do not attempt to create a column for revenue using SQL. This will be computed in Python post-processing

- If the user asks for **reorder placement date**, **when to reorder**, or **when should SKU be restocked**:
      Return:
      `SELECT * FROM report;`
- Do not attempt to create a column for reorder date using SQL. This will be computed in Python post-processing.


- If the user asks for **number of rows**, use:  
  `SELECT * FROM report;`

- If the user asks for **number of columns** or **column labels** or **column heading**, use:  
  `PRAGMA table_info(report);` 

- If the user asks for **SKU range**, use:  
  `SELECT DISTINCT(SKU) FROM report;`

- If the user asks for what is **brief summary** / **current inventory level**?
`SELECT *
  FROM report;`

- There is no difference between SKU-1, SKU1 and SKU-01. All to be treated same.

- If the user asks for what is **brief summary** / **current inventory level** of the sku-1 ?
`SELECT *
  FROM report
  where SKU = 'SKU-1';`


- If the user asks for list all SKUs whose expiry date is before  10th August?
`SELECT *
  FROM report
  where expiry_date <= '2025-08-10';`

- If the user asks for list all SKUs whose safety stock is less than 20% of its current inventory?
`SELECT *
  FROM report
  where safety_stock < 0.2 * Inventory ;`

- If the user asks for what is the expected loss in next one week?
  `SELECT * FROM report
    where expiry_date BETWEEN DATE('now') AND Date('now', '+7 days');`






- Avoid using subqueries unless absolutely necessary.  
- Assume all relevant columns are available directly in the `report` table.  Do not create new columns.
- Do not use table aliases like `r.` unless they are explicitly defined in the query.    



---
Write the correct SQLite query for:

Question: {user_input}

Return only the valid SQLite query. Do not prefix or explain anything. Do not say 'Here is the query:' or any other sentence. Just start from SELECT or PRAGMA.
"""


