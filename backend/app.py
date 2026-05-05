from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from GCP Backend 🚀"

@app.route("/api")
def api():
    return {"message": "API is working 🎯"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)