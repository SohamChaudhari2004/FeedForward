from app.models import mongo

'''
handles all the rewuests for food made by the recipients
'''

class Request:
    def __init__(self, user_id, food_id, status='Pending'):
        
        self.user_id = user_id
        self.food_id = food_id
        self.status = status

    @staticmethod
    def create_request(user_id ,food_id):

        request_data = {
            'user_id' : user_id,
            'food_id' : food_id,
            'status' : 'pending'
        }

        mongo.db.requests.insert_one(request_data)

    @staticmethod
    def get_request_by_user(user_id):
        return mongo.db.requests.find({"user_id": user_id})
    

    @staticmethod
    def get_request_by_id(request_id):
        return mongo.db.requests.find_one({"_id":request_id})

    @staticmethod
    def update_request_status(request_id,status):
        return mongo.db.requests.update_one({"_id": request_id}, {"$set": {"status":status}})
