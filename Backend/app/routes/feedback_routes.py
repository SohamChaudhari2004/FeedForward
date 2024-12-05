from flask import Blueprint , request  , jsonify
from app.models.feedback import Feedback

feedback_bp = Blueprint("feedback", __name__)

@feedback_bp.route('/<string:delivery_id>', methods=["GET"])
def get_feedback(delivery_id):
    feedbacks = Feedback.get_feedback_by_delivery(delivery_id)
    return jsonify(feedbacks)

@feedback_bp.route('/get-all', methods=["GET"])
def get_all_feedback(delivery_id):
    feedback_list = Feedback.get_all_feedback_for_delivery(delivery_id)
    return jsonify(feedback_list)

@feedback_bp.route('/', methods=["POST"])
def add_feedback():
    data = request.json
    user_id = data.get("user_id")
    delivery_id = data.get("delivery_id")
    rating = data.get("rating")
    comments = data.get("comments")
    if not(user_id and delivery_id and rating and comments):
        return jsonify({"message": "Missing required fields"}), 400
    Feedback.add_feedback(user_id, delivery_id, rating , comments)
    return jsonify({"message": "Feedback added successfully"}), 201
