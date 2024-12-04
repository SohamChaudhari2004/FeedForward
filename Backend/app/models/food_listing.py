from app.models import mongo

'''
Class for CRUD Operations for food listings
'''

class FoodListing:
    def __init__(self, donor_id, food_name, quantity, expiration_date, description):
        self.donor_id = donor_id
        self.food_name = food_name
        self.quantity = quantity
        self.expiration_date = expiration_date
        self.description = description

    @staticmethod
    def add_food_listing( donor_id, food_name, quantity, expiration_date, description):

        food_data = {
            "donor_id": donor_id,
            "food_name": food_name,
            "quantity": quantity,
            "expiration_date": expiration_date,
            "description": description

        }

        mongo.db.food_listings.insert_one(food_data)

    @staticmethod
    def get_food_listings():
        '''
        return all the food listings
        '''
        return list(mongo.db.food_listings.find())
    
    @staticmethod
    def get_food_listing_by_id(listing_id):
        ''' fetch the food listing by the id on mongodb '''
        return mongo.db.food_listings.find_one({"_id": listing_id})
    
    @staticmethod
    def delete_food_listing(listing_id):
        
        return mongo.db.food_listings.delete_one({"_id":listing_id})