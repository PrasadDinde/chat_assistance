from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def query_db(query, params=()):
    """Executes SQL query and returns results."""
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("query", "").lower()

    if "employees in" in user_input:
        dept = user_input.split("in")[-1].strip()
        result = query_db("SELECT Name FROM Employees WHERE Department=?", (dept,))
        return jsonify({"response": [row[0] for row in result]})

    elif "manager of" in user_input:
        dept = user_input.split("of")[-1].strip()
        result = query_db("SELECT Manager FROM Departments WHERE Name=?", (dept,))
        return jsonify({"response": result[0][0] if result else "Department not found"})

    elif "hired after" in user_input:
        date = user_input.split("after")[-1].strip()
        result = query_db("SELECT Name FROM Employees WHERE Hire_Date > ?", (date,))
        return jsonify({"response": [row[0] for row in result]})

    elif "total salary expense for" in user_input:
        dept = user_input.split("for")[-1].strip()
        result = query_db("SELECT SUM(Salary) FROM Employees WHERE Department=?", (dept,))
        return jsonify({"response": result[0][0] if result[0][0] else "No data found"})

    else:
        return jsonify({"response": "I couldn't understand your query. Try again!"})

if __name__ == "__main__":
    app.run(debug=True)
