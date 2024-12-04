from flask import Flask , jsonify
from flask_jwt_extended import JWTManager
from app.models import init_app
import os
from dotenv import load_dotenv






load_dotenv()
app = Flask(__name__)


app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"]= os.getenv("SECRET_KEY")


# Register blueprints




# check if teh routes are running properly
def health_check():
    return jsonify({'status': "success" , "message": "API is running"}) ,200 


if __name__ == "__main__":
    port  = os.getenv("PORT")
    app.run(debug=True , port=port)