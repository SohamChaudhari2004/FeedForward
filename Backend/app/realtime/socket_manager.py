from . import socketio
from flask_socketio import emit, join_room, leave_room
from app.realtime.location_service import update_location


@socketio.on("connect")
def handle_connect():
    """Handle a client connecting to the WebSocket."""
    emit("message", {"message": "Connected to the real-time server!"})
    print("A client connected.")


@socketio.on("disconnect")
def handle_disconnect():
    """Handle a client disconnecting from the WebSocket."""
    print("A client disconnected.")


@socketio.on("join_room")
def handle_join_room(data):
    """Handle a client joining a specific room."""
    room = data.get("room")
    if not room:
        emit("error", {"message": "Room name is required"})
        return
    join_room(room)
    emit("message", {"message": f"Joined room: {room}"}, room=room)


@socketio.on("leave_room")
def handle_leave_room(data):
    """Handle a client leaving a specific room."""
    room = data.get("room")
    if not room:
        emit("error", {"message": "Room name is required"})
        return
    leave_room(room)
    emit("message", {"message": f"Left room: {room}"}, room=room)


@socketio.on("broadcast")
def handle_broadcast(data):
    """Broadcast a message to all clients."""
    message = data.get("message")
    if not message:
        emit("error", {"message": "Message is required"})
        return
    emit("broadcast", {"message": message}, broadcast=True)


@socketio.on("update_location")
def handle_update_location(data):
    """Handle updating a user's location."""
    room = data.get("room")
    location = data.get("location")
    if not room or not location:
        emit("error", {"message": "Room and location data are required"})
        return

    # Update location using a service or logic
    update_location(room, location)

    # Notify room members about the location update
    emit("location_update", {"location": location}, room=room)