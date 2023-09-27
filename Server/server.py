from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route("/testing")
def sendMessage():
    print("Connected!")
    return jsonify({"message": "Hello World!"})

if __name__ == "__main__":
    app.run(debug=True)