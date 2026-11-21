"""
Simple Flask application for the AWS multi-region project.

This is a recreated sample based on the routes described in the project
documentation. It is not claimed to be the exact original demo-app.py file.
"""

import os

from flask import Flask, jsonify

app = Flask(__name__)

# Set AWS_REGION_NAME to "Mumbai" or "Hyderabad" on each server.
REGION_NAME = os.getenv("AWS_REGION_NAME", "Mumbai")


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the AWS Multi-Region Flask Application",
        "region": REGION_NAME,
        "status": "running"
    })


@app.route("/region")
def region():
    return jsonify({
        "region": REGION_NAME,
        "message": f"Application is running in {REGION_NAME}"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "region": REGION_NAME
    })


if __name__ == "__main__":
    # 0.0.0.0 allows the application to be reached from outside the VM.
    app.run(host="0.0.0.0", port=5000, debug=False)
