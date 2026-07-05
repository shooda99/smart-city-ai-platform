from flask import Flask, render_template, request, jsonify
from vertex_helper import ask_llm
from bigquery_helper import execute_query
from sql_generator import generate_sql
import os
app = Flask(__name__)
LOOKER_URL = "https://datastudio.google.com/embed/reporting/01279ffd-ee42-4c2a-8f52-38ae62bd336c/page/sGx2F"

@app.route("/")
def home():
   return render_template("index.html", looker_url=LOOKER_URL)

@app.route("/ask", methods=["POST"])
def ask():
   question = request.json.get("question", "").strip()
   if not question:
       return jsonify({
           "answer": "Please enter a question."
       })
   try:
       # Step 1 - English -> SQL
       sql = generate_sql(question)
       print("Generated SQL:")
       print(sql)
       # Step 2 - Execute SQL
       result = execute_query(sql)
       # Step 3 - SQL Result -> English
       answer = ask_llm(question, result)
       return jsonify({
           "answer": answer
       })
   except Exception as e:
       return jsonify({
           "answer": str(e)
       })

if __name__ == "__main__":
   port = int(os.environ.get("PORT", 8080))
   app.run(
       host="0.0.0.0",
       port=port
   )