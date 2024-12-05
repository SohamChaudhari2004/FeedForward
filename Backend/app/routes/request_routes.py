from flask import Blueprint, jsonify, request
from app.models.request import Request

request_bp = Blueprint("requests", __name__)

# Route: Get all requests
@request_bp.route("/", methods=["GET"], endpoint="get_all_requests")
def get_requests():
    requests = Request.objects()
    return jsonify({"requests": requests}), 200

# Route: Create a new request
@request_bp.route("/", methods=["POST"], endpoint="create_request")
def create_request():
    data = request.get_json()
    new_request = Request(**data)
    new_request.save()
    return jsonify({"message": "Request created successfully"}), 201

# Route: Get a specific request by ID
@request_bp.route("/<request_id>", methods=["GET"], endpoint="get_request_by_id")
def get_request(request_id):
    req = Request.objects(id=request_id).first()
    if not req:
        return jsonify({"error": "Request not found"}), 404
    return jsonify({"request": req}), 200

# Route: Update a request by ID
@request_bp.route("/<request_id>", methods=["PUT"], endpoint="update_request")
def update_request(request_id):
    data = request.get_json()
    req = Request.objects(id=request_id).first()
    if not req:
        return jsonify({"error": "Request not found"}), 404
    req.update(**data)
    return jsonify({"message": "Request updated successfully"}), 200

# Route: Delete a request by ID
@request_bp.route("/<request_id>", methods=["DELETE"], endpoint="delete_request")
def delete_request(request_id):
    req = Request.objects(id=request_id).first()
    if not req:
        return jsonify({"error": "Request not found"}), 404
    req.delete()
    return jsonify({"message": "Request deleted successfully"}), 200
