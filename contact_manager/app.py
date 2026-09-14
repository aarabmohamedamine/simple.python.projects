from flask import Flask, render_template, request, jsonify
from operations import ContactManager

app = Flask(__name__)
manager = ContactManager()   # instance we7da

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/contacts", methods=["GET"])
def get_contacts():
    return jsonify(manager.get_all_contacts())

@app.route("/api/contacts", methods=["POST"])
def add_contact():
    d = request.json
    new_id = manager.add_contact_api(d["user_name"], d["phone"], d["email"])
    return jsonify({"id": new_id}), 201

@app.route("/api/contacts/<int:cid>", methods=["PUT"])
def update_contact(cid):
    d = request.json
    manager.update_contact_api(cid, d["user_name"], d["phone"], d["email"])
    return jsonify({"ok": True})

@app.route("/api/contacts/<int:cid>", methods=["DELETE"])
def delete_contact(cid):
    manager.delete_contact_api(cid)
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(debug=True)