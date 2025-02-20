#!/usr/bin/python3
"""Develop a Simple API using Python with Flask"""

from flask import Flask, jsonify, request

app = Flask(__name__)
# In-memory user storage
users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data['username']
    users[username] = data
    return jsonify({"message": "user added", "user": data}), 201


if __name__ == "__main__":
    app.run(debug=True)
