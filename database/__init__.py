from motor.motor_asyncio import AsyncIOMotorClient
# from config.urls import urls  # Ensure this imports your settings correctly
from config.settings import config
# from pydantic import BaseSettings
from pydantic_settings import BaseSettings

# Define your settings class
class Settings(BaseSettings):
    mongodb_uri: str  # New field for MongoDB URI
    database_db: str  # Ensure you have the database name here if you need it

    class Config:
        env_file = ".env"  # Load environment variables from .env file
        extra = "allow" 

# Load settings
settings = Settings()

# Initialize MongoDB client using the connection string
client = AsyncIOMotorClient(settings.mongodb_uri)  # Use the connection string from settings
print(client.server_info())  
# Access your specified database
db = client[settings.database_db]

# Optional helper function to get a MongoDB collection
def get_collection(collection_name: str):
    return db[collection_name]



# from motor.motor_asyncio import AsyncIOMotorClient
# from config.urls import urls

# # Initialize MongoDB client
# client = AsyncIOMotorClient(urls.mongodb_uri)

# # Access your specified database
# db = client[urls.database_db]

# # Optional helper function to get a MongoDB collection
# def get_collection(collection_name: str):
#     return db[collection_name]






# from config.urls import urls

# from .base_model import Base, BaseModel
# from .create_database import SQLDatabase
# from .models import Users


# db_object = SQLDatabase(urls.postgres_database_conn_str)
