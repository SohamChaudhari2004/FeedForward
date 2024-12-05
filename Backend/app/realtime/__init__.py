from flask_socketio import SocketIO


socketio = SocketIO(cors_allowed_origins="*")


def init_realtime(app):
    """Attach the SocketIO instance to the Flask app."""
    socketio.init_app(app)