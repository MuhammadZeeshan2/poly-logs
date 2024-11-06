from pydantic import BaseModel, Field  # Import Field from pydantic
from datetime import datetime
from typing import List, Optional

class ResourceCreatedResponse(BaseModel):
    detail: str
    id: str  # MongoDB ObjectId as string

class ResourceDeletedResponse(BaseModel):
    detail: str

class ConflictDetail(BaseModel):
    detail: str

class UserSchema(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    username: str
    email: str
    age: Optional[int] = None

    class Config:
        json_encoders = {
            "_id": str
        }

class LogResponse(BaseModel):
    id: str
    log_type: str
    service: str
    level: str
    timestamp: datetime
    message: str
    details: Optional[dict]

class LogListResponse(BaseModel):
    logs: List[LogResponse]
    count: int

# Additional schemas for listing users or updating them as needed
class UserListResponse(BaseModel):
    users: List[UserSchema]  # Changed from list to List for consistency
    count: int


# from pydantic import BaseModel


# class ResourceCreatedResponse(BaseModel):
#     detail: str
#     id: int


# class ResourceDeletedResponse(BaseModel):
#     detail: str


# class ConflictDetail(BaseModel):
#     detail: str
