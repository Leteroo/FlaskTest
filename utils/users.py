"""
檔名就是 API 前綴，這邊只定義 API 後綴(含起始斜線)
"""
from flask import jsonify, request, Blueprint

bp_users = Blueprint("api", __name__)

# 模擬資料庫
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# GET /users
@bp_users.route("", methods=["GET"])
def get_users():
    return jsonify(users)

# GET /users/<id>
@bp_users.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST /users
@bp_users.route("", methods=["POST"])
def add_user():
    data = request.get_json()
    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data["name"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT /users/<id>
@bp_users.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        user["name"] = data.get("name", user["name"])
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# DELETE /users/<id>
@bp_users.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"})