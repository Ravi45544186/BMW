from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory data storage (just for this example)
data = [
    {"id": 1, "name": "John", "age": 30},
    {"id": 2, "name": "Jane", "age": 25}
]

# 1. GET Request - Retrieve Data
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"data": data})

# 2. POST Request - Add Data
@app.route('/api/data', methods=['POST'])
def add_data():
    new_data = request.get_json()  # Get data from request body
    new_id = max([item["id"] for item in data], default=0) + 1  # Generate new ID
    new_data["id"] = new_id
    data.append(new_data)
    return jsonify({"message": "Data added successfully", "data": new_data}), 201

# 3. PUT Request - Update Data
@app.route('/api/data/<int:data_id>', methods=['PUT'])
def update_data(data_id):
    # Find the item in data list
    item = next((item for item in data if item["id"] == data_id), None)
    
    if item is None:
        return jsonify({"message": "Data not found"}), 404
    
    updated_data = request.get_json()  # Get updated data from request
    item.update(updated_data)  # Update the item
    return jsonify({"message": "Data updated successfully", "data": item}), 200

# 4. DELETE Request - Delete Data
@app.route('/api/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    # Find the item in data list
    item = next((item for item in data if item["id"] == data_id), None)
    
    if item is None:
        return jsonify({"message": "Data not found"}), 404
    
    data.remove(item)  # Remove the item
    return jsonify({"message": "Data deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
