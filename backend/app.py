from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 🔥 this line fixes CORS

@app.route("/")
def home():
    return "Hello from GCP Backend 🚀"

@app.route("/api")
def api():
    return jsonify({"message": "API is working 🎯"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)