from flask import Flask, request, jsonify
import calculator

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Calculator API!"

@app.route("/add")
def add():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=calculator.add(a, b))

@app.route("/subtract")
def subtract():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=calculator.subtract(a, b))

@app.route("/multiply")
def multiply():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=calculator.multiply(a, b))

@app.route("/divide")
def divide():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=calculator.divide(a, b))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
