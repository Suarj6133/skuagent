from flask import Flask, request, render_template, redirect, url_for, session, send_file
from llm_agent import get_sql_from_llama
from query_handler import process_user_query
import pandas as pd
import sqlite3
import io

app = Flask(__name__)
app.secret_key = 'super-secret-key'
DB_PATH = "grocery_data.db"

@app.route("/", methods=["GET", "POST"])
def home():
    if "history" not in session:
        session["history"] = []

    if request.method == "POST":
        if "clear" in request.form:
            session["history"] = []
            session.pop("last_df", None)
            return redirect(url_for("home"))

        question = request.form["question"]
        sql = get_sql_from_llama(question)
        result_html = ""
        note = ""

        try:
            # Run SQL query once
            conn = sqlite3.connect(DB_PATH)
            df = pd.read_sql_query(sql, conn)
            conn.close()

            # Store original query result in session
            session["last_df"] = df.to_json(orient="split")

            result_html += "<h4>🔍 SQL Query Result:</h4>"
            result_html += df.to_html(classes="styled-table", index=False)

            # Delegate to analysis logic
            analysis_df = process_user_query(question, sql, df)

            if analysis_df is not None:
                result_html += f"<h4>🛠️ Analysis Based On:</h4><p><em>{question}</em></p>"
                result_html += analysis_df.to_html(classes="styled-table", index=False)
                session["last_df"] = analysis_df.to_json(orient="split")

        except Exception as e:
            result_html = f"<p class='error'>❌ Error: {e}</p>"

        session["history"].append({
            "question": question,
            "sql": sql,
            "answer": result_html,
            "note": note
        })
        session.modified = True

    return render_template("index.html", history=session.get("history", []))


@app.route("/download")
def download():
    if "last_df" not in session:
        return "No data to download", 400

    df = pd.read_json(session["last_df"], orient="split")

    # Write DataFrame to Excel
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Results")
    output.seek(0)

    return send_file(
        output,
        as_attachment=True,
        download_name="result.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


if __name__ == "__main__":
    app.run(debug=True)
