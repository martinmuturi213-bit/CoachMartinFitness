import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)


@app.route("/")
def home():
    return send_from_directory('.', 'index.html')



@app.route("/register", methods=["POST"])
def register():

    name = request.form.get("name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    service = request.form.get("service")
    package = request.form.get("package")
    goal = request.form.get("goal")

    print("\n===== NEW CLIENT =====")
    print("Name:", name)
    print("Phone:", phone)
    print("Email:", email)
    print("Service:", service)
    print("Package:", package)
    print("Goal:", goal)
    print("======================\n")

    return jsonify({
        "success": True,
        "message": "Registration received successfully!"
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 1000))
    app.run(host='0.0.0.0', port=port)
