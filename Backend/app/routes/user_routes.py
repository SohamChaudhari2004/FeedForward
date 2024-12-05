from flask import Blueprint, jsonify, request
from app.models.user import User

user_bp = Blueprint("users", __name__)

# Route: Get all users
@user_bp.route("/", methods=["GET"], endpoint="get_all_users")
def get_users():
    users = User.objects()
    return jsonify({"users": users}), 200

# Route: Create a new user
@user_bp.route("/", methods=["POST"], endpoint="create_user")
def create_user():
    data = request.get_json()
    user = User(**data)
    user.save()
    return jsonify({"message": "User created successfully"}), 201

# Route: Get a specific user by ID
@user_bp.route("/<user_id>", methods=["GET"], endpoint="get_user_by_id")
def get_user(user_id):
    user = User.objects(id=user_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"user": user}), 200

# Route: Update a user by ID
@user_bp.route("/<user_id>", methods=["PUT"], endpoint="update_user")
def update_user(user_id):
    data = request.get_json()
    user = User.objects(id=user_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    user.update(**data)
    return jsonify({"message": "User updated successfully"}), 200

# Route: Delete a user by ID
@user_bp.route("/<user_id>", methods=["DELETE"], endpoint="delete_user")
def delete_user(user_id):
    user = User.objects(id=user_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    user.delete()
    return jsonify({"message": "User deleted successfully"}), 200
