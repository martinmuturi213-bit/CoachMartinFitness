  from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

@app.route("/<path:filename>")
def files(filename):
    return send_from_directory('.', filename)

@app.route("/register", methods=["POST"])
def register():
    print("New client:", request.form.get("name"))
    return jsonify({"success": True})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
