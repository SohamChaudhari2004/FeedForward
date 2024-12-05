from flask import Blueprint , request , jsonify
from app.models.food_listing import FoodListing

food_bp = Blueprint("food" , __name__)

@food_bp.route("/", methods = ["GET"])
def get_all_food_listings():
    food_list  = FoodListing.get_food_listings()
    return jsonify(food_list)

@food_bp.route("/add-food", methods = ["POST"])
def add_food_listing():
    data = request.json
    required_fields = ['donr_id' , 'food_name' , 'quantity', 'expiration_date', 'description']
    if not all(field in data for field in required_fields):
        return jsonify({"message": "Missing required fields"}), 400
    
    FoodListing.add_food_listing(**data)
    return jsonify({"message": "Food listing added successfully"}), 201

@food_bp.route("/<string:listing_id>", methods = ["POST"])
def delete_food_listings(listing_id):
    FoodListing.delete_food_listing(listing_id)
    return jsonify({"message": "Food listing deleted successfully"})


@food_bp.route("/<string:listing_id>", methods = ["POST"])
def get_food_listing_by_id(listing_id):
    food  = FoodListing.get_food_listing_by_id(listing_id)
    return jsonify(food)
