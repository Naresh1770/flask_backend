
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    data = request.get_json(silent=True) or {}

    item_name = data.get("itemName")
    item_description = data.get("itemDescription")

    if not item_name or not item_description:
        return jsonify({"error": "Both fields are required"}), 400

    print("Item Name:", item_name)
    print("Item Description:", item_description)

    return jsonify({
        "message": "To-Do item submitted successfully",
        "itemName": item_name,
        "itemDescription": item_description
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
