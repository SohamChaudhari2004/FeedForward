location_data = {}  # Temporary in-memory storage for location updates

def update_location(room, location):
    """Update the location for a specific room."""
    location_data[room] = location