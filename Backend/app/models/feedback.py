from app.models import mongo

''' add and get feeback for deliveries  '''

class Feedback:
    def __init__(self, user_id , delivery_id , rating , comments):
        self.user_id = user_id
        self.delivery_id = delivery_id
        self.rating = rating
        self.comments = comments

    @staticmethod
    def add_feedback(user_id , delivery_id , rating , comments):

        feedback_data = {
            "user_id": user_id,
            "delivery_id": delivery_id,
            "rating": rating,
            "comments": comments,
        }
        
        mongo.db.feedback.insert_one(feedback_data)


    @staticmethod
    def get_feedback_by_delivery(delivery_id):
        return list(mongo.db.feedback.find({"delivery_id": delivery_id}))


    @staticmethod
    def get_all_feedback_for_delivery(delivery_id):
        return list(mongo.db.feedback.find({"delivery_id": delivery_id}))

