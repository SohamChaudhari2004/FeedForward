import os

class Config:
    """Base configuration class."""
    SECRET_KEY = os.getenv("SECRET_KEY", "secret_key")
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/food_saver")
    DEBUG = os.getenv("DEBUG", "True").lower() in ["true", "1", "yes"]
