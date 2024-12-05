from flask_socketio import emit, join_room, leave_room
from app.realtime.location_service import update_location

def register_socket_events(socketio):
    """Register Socket.IO events."""

    @socketio.on("join")
    def handle_join(data):
        room = data.get("room")
        join_room(room)
        emit("status", {"message": f"Joined room {room}"}, room=room)

    @socketio.on("leave")
    def handle_leave(data):
        room = data.get("room")
        leave_room(room)
        emit("status", {"message": f"Left room {room}"}, room=room)

    @socketio.on("update_location")
    def handle_update_location(data):
        room = data.get("room")
        location = data.get("location")
        if not location:
            emit("error", {"message": "Invalid location data"}, room=room)
            return
        update_location(room, location)
        emit("location_update", {"location": location}, room=room)
