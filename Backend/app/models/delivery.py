from app.models import mongo

''' 
contains details about the delivery status time location id
'''

class Delivery:
    def __init__(self,request_id ,delivery_status , delivery_time , location):
        self.request_id = request_id
        self.delivery_status = delivery_status
        self.delivery_time = delivery_time
        self.location= location

    @staticmethod
    def create_delivery(request_id, delivery_time , location):
        ''' create teh data to be sent in each delivery'''
        delivery_data = {
            "request_id": request_id,
            "delivery_status": "pending",
            "delivery_time": delivery_time,
            "location": location,
        }
        mongo.db.deliveries.insert_one(delivery_data)


    @staticmethod
    def get_delivery_by_request(request_id):
        return mongo.db.deliveries.find_one({"request_id": request_id})

    @staticmethod
    def update_delivery_status(delivery_id , status , location):
        return mongo.db.deliveries.update_one({"_id": delivery_id}, {"$set": {"delivery_status": status , "location": location}})