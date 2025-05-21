from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify({'sum': a + b})
    except (TypeError, ValueError):
        return jsonify({'error': 'Please provide valid numbers as query parameters `a` and `b`.'}), 400
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
