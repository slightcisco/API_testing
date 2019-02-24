from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/json/") # adding this about a function allows for a URI endpoint
def jsonHello():
    return jsonify({"about": "Hello World"})

@app.route("/")
def htmlHello():
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True)
