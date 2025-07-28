Summary of model
This model gives real time answers for day to day planning of sku which can frequenty expiry date(perishable items). 

(a) column label:
SKU , Inventory, daily order quantity, expiry date ,unit price, reorder time, safety stock (inventory/daily order qty + 10% as safety margin)

(b) Requirements Ollama (as LLM) before proceeding ahead. If using chatGPT/ Gemini make changes in the llm_agent.py

(c) the data is grocery_data.xlsx file
(d) the data is loaded into the db and then query is perfomred.
(e) For advance analysis- Python is integrating in to analysis.py

(f) for running - install ollama -> type python load_csv.py in terminal - > python app.py in terminal and start!! 

(g) start aksing questing like brief summary of mdodel 
List skus with expiry date , expected loss , when to reorder
