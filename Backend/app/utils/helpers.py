def format_response(data, message="Success"):
    """Standardize API responses."""
    return {"message": message, "data": data}
