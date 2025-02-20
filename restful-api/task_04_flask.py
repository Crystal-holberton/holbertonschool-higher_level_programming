from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage (Start with empty dictionary)
users = {}

# Root endpoint
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Status endpoint
@app.route('/status')
def status():
    return "OK"

# Retrieve all usernames
@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))

# Retrieve a specific user by username
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400
    
    print("Received data:", data)  # Debugging
    
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data["username"]
    if username in users:
        print("Existing users:", users.keys())  # Debugging
        return jsonify({"error": "User already exists"}), 400
    
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(debug=True)
