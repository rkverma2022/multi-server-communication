from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

# HTML Template for the root page
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Real Estate Main Server</title>
</head>
<body> 
    <h2>Choose Operation</h2>
    <form action="/compute" method="get">
        <label for="a">A:</label>
        <input type="number" name="a" required><br><br>

        <label for="b">B:</label>
        <input type="number" name="b" required><br><br>

        <label for="operation">Operation:</label>
        <select name="operation">
            <option value="add">Add</option>
            <option value="divide">Divide</option>
            <option value="multiply">Multiply</option>
        </select><br><br>

        <input type="submit" value="Calculate">
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_FORM)

@app.route('/compute')
def compute():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    operation = request.args.get('operation')

    return handle_operation(operation, a, b)

@app.route('/<operation>')
def dynamic_operation(operation):
    # Example: /add?a=9&b=3
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return handle_operation(operation, a, b)

def handle_operation(operation, a, b):
    endpoints = {
        "add": ("http://localhost:5000/add", "sum", "+"),
        "divide": ("http://localhost:8080/divide", "result", "/"),
        "multiply": ("http://localhost:3000/multiply", "result", "*"),
    }

    if operation not in endpoints:
        return "Invalid operation", 400

    url, key, symbol = endpoints[operation]
    try:
        res = requests.get(url, params={"a": a, "b": b})
        data = res.json()
        result = data[key]
        return f"{a} {symbol} {b} = {result}"
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)

