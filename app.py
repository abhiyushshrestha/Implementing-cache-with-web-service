from flask import Flask, request, jsonify
import config

app = Flask(__name__)
@app.route("/")
def start():
    return "Hello world"

@app.route('/data')
def data():
    return config.data

@app.route('/books')
def books():
    return jsonify(config.books)

@app.route('/a')
def a():
    return "a"

@app.route('/b')
def b():
    return "b"

@app.route('/c')
def c():
    return "c"

@app.route('/d')
def d():
    return "d"


if __name__ == "__main__":
    app.debug = True
    app.run()