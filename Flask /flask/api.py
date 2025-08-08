from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

items = [
    {"id": 1, "item": "item1", "description": "This is item 1"},
    {"id": 2, "item": "item2", "description": "This is item 2"},
]

@app.route('/')
def home():
    return "Welcome to the sample To-Do List application!"

@app.route("/items", methods=['GET'])
def get_items():
    return jsonify(items)

@app.route("/items/<int:item_id>", methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

@app.route("/items", methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({"error": "Bad Request"}), 400
    new_id = items[-1]["id"] + 1 if items else 1
    new_item = {
        "id": new_id,
        "item": request.json['name'],
        "description": request.json.get('description', '')
    }
    items.append(new_item)
    return jsonify(new_item), 201

@app.route("/items/<int:item_id>", methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    item['item'] = request.json.get('name', item['item'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

@app.route("/items/<int:item_id>", methods=['DELETE'])
def delete_item(item_id):
    global items
    new_items = [item for item in items if item["id"] != item_id]
    if len(new_items) == len(items):
        return jsonify({"error": "Item not found"}), 404
    items = new_items
    return jsonify({"result": "Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)
