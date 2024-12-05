from flask import Flask , jsonify
from flask_jwt_extended import JWTManager
from app.models import init_app
from app.routes.delivery_routes import delivery_bp
from app.routes.food_routes import food_bp
from app.routes.request_routes import request_bp
from app.routes.user_routes import user_bp
from app.routes.feedback_routes import feedback_bp
import os
from dotenv import load_dotenv
from app.realtime import socketio, init_realtime
from app.realtime.socket_events import register_socket_events

load_dotenv()
app = Flask(__name__)


app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"]= os.getenv("SECRET_KEY")


# Initialize other modules (models, routes, etc.)
init_app(app)

init_realtime(app)
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(user_bp ,url_prefix = '/users')
app.register_blueprint(delivery_bp ,url_prefix = '/delivery')
app.register_blueprint(request_bp ,url_prefix = '/requests')
app.register_blueprint(feedback_bp ,url_prefix = '/feedback')
app.register_blueprint(food_bp ,url_prefix = '/foodlistings')


# Register Socket.IO events
register_socket_events(socketio)

# check if teh routes are running properly
def health_check():
    return jsonify({'status': "success" , "message": "API is running"}) ,200 


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
    health_check()