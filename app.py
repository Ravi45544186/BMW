from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for demonstration (you can replace this with a real database later)
database = [
    {"id": 1, "name": "John", "age": 30},
    {"id": 2, "name": "Jane", "age": 25}
]

# Create a new entry (C - Create)
@app.route('/api/data', methods=['POST'])
def create_data():
    new_data = request.get_json()
    database.append(new_data)  # Save to in-memory database
    return jsonify({"message": "Data created successfully!", "data": new_data}), 201


# Read all entries (R - Read)
@app.route('/api/data', methods=['GET'])
def get_all_data():
    return jsonify({"data": database})


# Read a specific entry (R - Read)
@app.route('/api/data/<int:id>', methods=['GET'])
def get_data(id):
    if id < len(database):
        return jsonify({"data": database[id]})
    return jsonify({"message": "Data not found!"}), 404


# Update an entry (U - Update)
@app.route('/api/data/<int:id>', methods=['PUT'])
def update_data(id):
    if id < len(database):
        updated_data = request.get_json()
        database[id] = updated_data  # Update the in-memory database
        return jsonify({"message": "Data updated successfully!", "data": updated_data})
    return jsonify({"message": "Data not found!"}), 404


# Delete an entry (D - Delete)
@app.route('/api/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    if id < len(database):
        deleted_data = database.pop(id)
        return jsonify({"message": "Data deleted successfully!", "data": deleted_data})
    return jsonify({"message": "Data not found!"}), 404


if __name__ == '__main__':
    app.run(debug=True)
