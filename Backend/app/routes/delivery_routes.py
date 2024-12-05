from flask import request , Blueprint , jsonify
from app.models.delivery import Delivery

delivery_bp = Blueprint("delivery", __name__)

@delivery_bp.route('/', methods=['POST'])
def create_delivery():
    data = request.json
    request_id = data.get("request_id")
    delivery_time = data.get("delivery_time")
    location = data.get("location")
    if not (request_id and delivery_time and location):
        return jsonify({"message": "Missing required fields"}) , 400
    
    Delivery.create_delivery(request_id, delivery_time , location)
    return jsonify({"message": "delivery created successfully"}) , 201

@delivery_bp.route('/<string:request_id>', methods=["GET"])
def get_delivery(request_id):
    delivery = Delivery.get_delivery_by_request(request_id)

    return jsonify(delivery), 200

@delivery_bp.route('/<string:delivery_id>', methods=["GET"])
def update_delivery(delivery_id , status , location):
    data= request.json
    delivery_id = data.get("delivery_id")
    status = data.get("status")
    location = data.get("location")
    delivery = Delivery.update_delivery_status(delivery_id, status, location)

    return jsonify(delivery), 200