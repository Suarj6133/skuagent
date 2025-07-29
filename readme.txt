# 🧠 AI Grocery Agent — LLM + Python

This project is an AI-powered assistant designed to answer real-time, natural language questions related to SKU (Stock Keeping Unit) planning for perishable grocery items. It helps optimize inventory management, reduce waste, and make better reorder decisions using a local LLM (Ollama) integrated with Python.

## 📌 Summary of the Model

This model provides real-time answers for day-to-day planning of grocery SKUs, especially those with short shelf lives (perishable items). It uses a local language model (via Ollama) to interpret natural language queries and provide structured, actionable insights from a backend database.

---

## 🗂️ Dataset Overview

### Column Labels:
- `SKU`: Item identifier
- `Inventory`: Current stock
- `Daily Order Quantity`: Avg. daily demand
- `Expiry Date`: When the product expires
- `Unit Price`: Cost per item
- `Reorder Time`: Time needed to restock
- `Safety Stock`: *(Inventory / Daily Order Qty) + 10% buffer*

---

## ⚙️ Requirements

- Python 3.10+
- [Ollama](https://ollama.com) (required to run the LLM locally)

> 💡 If you prefer using ChatGPT or Gemini APIs instead of Ollama, modify `llm_agent.py` accordingly.

---

## 📁 Data Input

- Input file: `grocery_data.xlsx`
- Data is loaded and converted into SQLite format (`grocery_data.db`) using `load_csv.py`

---

## 🧠 How It Works

1. Natural language questions are interpreted via LLM (Ollama).
2. The query handler and prompt builder convert user input into meaningful database queries.
3. Python functions in `analysis.py` offer advanced calculations (e.g., expected loss, reorder planning).
4. The agent returns concise, helpful responses based on structured data.

---

## 🚀 Getting Started

### Step-by-Step Instructions:

```bash
# Step 1: Install Ollama
https://ollama.com/download

# Step 2: Load the dataset into the database
python load_csv.py

# Step 3: Launch the AI agent
python app.py
