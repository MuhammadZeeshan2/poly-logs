from motor.motor_asyncio import AsyncIOMotorCollection
from typing import Optional
from api.schemas import UserSchema
from bson import ObjectId
from database import get_collection
from bson.errors import InvalidId
class UserService:
    def __init__(self):
        self.collection: AsyncIOMotorCollection = get_collection("users")

    async def user_exists(self, username: Optional[str] = None, email: Optional[str] = None) -> bool:
        """Check if user exists by username or email."""
        query = {}
        if username:
            query["username"] = username
        elif email:
            query["email"] = email
        else:
            raise ValueError("You must provide either username or email")

        user = await self.collection.find_one(query)
        return user is not None

    async def create_user(self, user_data: dict) -> str:
        """Insert a new user into the collection and return the inserted ID."""
        result = await self.collection.insert_one(user_data)
        return str(result.inserted_id)
    
    async def get_user(self, user_id: str) -> Optional[UserSchema]:
        """Fetch a user by ID from the collection."""
        if not ObjectId.is_valid(user_id):
            raise ValueError(f"{user_id} is not a valid ObjectId.")
        
        user_data = await self.collection.find_one({"_id": ObjectId(user_id)})
        return UserSchema(**user_data) if user_data else None

    async def update_user(self, user_id: str, update_data: dict) -> bool:
        """Update a user by ID."""
        if not ObjectId.is_valid(user_id):
            raise ValueError(f"{user_id} is not a valid ObjectId.")
        
        result = await self.collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
        return result.modified_count > 0

    async def delete_user(self, user_id: str) -> bool:
        """Delete a user by ID."""
        if not ObjectId.is_valid(user_id):
            raise ValueError(f"{user_id} is not a valid ObjectId.")
        
        result = await self.collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0








# from sqlalchemy import select  # Import the select function
# from typing import Optional
# from api.base_service import BaseService  # Make sure BaseService is the updated, async version
# from database import Users

# class UserService(BaseService):  # Replace YourCreateSchema and YourUpdateSchema with the actual types
#     def __init__(self, db_object):
#         super().__init__(model=Users, db_object=db_object)

#     async def user_exists(self, username: Optional[str] = None, email: Optional[str] = None) -> bool | ValueError:
#         """Check if user exists"""
#         async with self.db_object.db() as session:  # Assuming db() is an async context manager
#             if username:
#                 stmt = select(self.model).where(self.model.username == username)
#                 result = await session.execute(stmt)
#                 user = result.scalar_one_or_none()
#             elif email:
#                 stmt = select(self.model).where(self.model.email == email)
#                 result = await session.execute(stmt)
#                 user = result.scalar_one_or_none()
#             else:
#                 raise ValueError("You must provide either username or email")
#             return True if user else False
