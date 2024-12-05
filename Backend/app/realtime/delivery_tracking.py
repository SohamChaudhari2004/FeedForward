from flask_socketio import emit
from . import socketio

@socketio.on("update_location")
def handle_update_location(data):
    """
    Handle real-time location updates for deliveries.
    
    Args:
        data (dict): Contains delivery_id and new location coordinates.
    """
    delivery_id = data.get("delivery_id")
    location = data.get("location")
    if not (delivery_id and location):
        emit("error", {"message": "Missing delivery_id or location"})
        return
    
    # Broadcast the updated location to clients in the delivery room
    emit("location_update", {"delivery_id": delivery_id, "location": location}, room=f"delivery_{delivery_id}")

@socketio.on("delivery_status")
def handle_delivery_status(data):
    """
    Handle real-time status updates for deliveries.
    
    Args:
        data (dict): Contains delivery_id and new status.
    """
    delivery_id = data.get("delivery_id")
    status = data.get("status")
    if not (delivery_id and status):
        emit("error", {"message": "Missing delivery_id or status"})
        return

    # Broadcast the updated status to clients in the delivery room
    emit("status_update", {"delivery_id": delivery_id, "status": status}, room=f"delivery_{delivery_id}")
