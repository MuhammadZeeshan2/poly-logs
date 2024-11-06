from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from api.constants import LogLevel,LogType

# Metadata schema to capture additional log details
class Metadata(BaseModel):
    user_id: Optional[str] = Field(None, description="User ID associated with the log entry")
    ip_address: Optional[str] = Field(None, description="IP address associated with the log")
    endpoint: Optional[str] = Field(None, description="API endpoint accessed")
    response_time_ms: Optional[int] = Field(None, description="Response time in milliseconds")
    stack_trace: Optional[str] = Field(None, description="Stack trace for error logs")
    error_code: Optional[str] = Field(None, description="Error code if applicable")
    transaction_id: Optional[str] = Field(None, description="Transaction or request ID")
    status_code: Optional[int] = Field(None, description="HTTP status code")

# Base model for common log fields
class LogBase(BaseModel):
    log_type: LogType = Field(..., description="Type of log (e.g., error, info)")
    service_name: str = Field(..., description="Service name producing the log")
    level: str = Field(..., description="Severity level (e.g., ERROR, INFO)")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of the log")
    message: str = Field(..., description="Log message")
    metadata: Optional[Metadata] = Field(None, description="Additional metadata for the log entry")

# Model for creating a log entry
class LogCreate(LogBase):
    pass

# Model for updating a log entry with optional fields
class LogUpdate(BaseModel):
    log_type: Optional[LogType] = Field(None, description="Type of log (e.g., error, info)")
    service_name: Optional[str] = Field(None, description="Service name producing the log")
    level: Optional[str] = Field(None, description="Severity level (e.g., ERROR, INFO)")
    timestamp: Optional[datetime] = Field(None, description="Timestamp of the log")
    message: Optional[str] = Field(None, description="Log message")
    metadata: Optional[Metadata] = Field(None, description="Additional metadata for the log entry")

# Model for log response
class LogResponse(LogBase):
    id: Optional[str] = Field(None, description="Log entry ID as a string")
    # log_type: Optional[LogType]

    service_name: Optional[str] = None
    @classmethod
    def from_mongo(cls, data: dict):
         
        """Helper to convert MongoDB document to LogResponse format."""
        if "_id" in data:
            data["id"] = str(data["_id"])  # Convert ObjectId to string
                # Convert log_type to LogType enum if it's present and is a valid string
        # if "log_type" in data:
        #     try:
        #         data["log_type"] = LogType(data["log_type"])  # Convert string to enum
        #     except ValueError:
        #         print(f"Invalid log type value: {data['log_type']}")  # Handle invalid log type
        #         data["log_type"] = LogType.INFO  # Set to a default value if desired

        return cls(**data)











# # models.py
# from pydantic import BaseModel, Field
# from typing import Optional
# from datetime import datetime
# from api.constants import LogType

# # Metadata schema to capture additional log details
# class Metadata(BaseModel):
#     user_id: Optional[str] = Field(None, description="User ID associated with the log entry")
#     ip_address: Optional[str] = Field(None, description="IP address associated with the log")
#     endpoint: Optional[str] = Field(None, description="API endpoint accessed")
#     response_time_ms: Optional[int] = Field(None, description="Response time in milliseconds")
#     stack_trace: Optional[str] = Field(None, description="Stack trace for error logs")
#     error_code: Optional[str] = Field(None, description="Error code if applicable")
#     transaction_id: Optional[str] = Field(None, description="Transaction or request ID")
#     status_code: Optional[int] = Field(None, description="HTTP status code")

# # Base model for common log fields
# class LogBase(BaseModel):
#     # log_type: str = Field(..., description="Type of log (e.g., error, info)")
#     log_type: LogType
#     service_name: str = Field(..., description="Service name producing the log")
#     level: str = Field(..., description="Severity level (e.g., ERROR, INFO)")
#     timestamp: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of the log")
#     message: str = Field(..., description="Log message")
#     metadata: Optional[Metadata] = Field(None, description="Additional metadata for the log entry")

# # Model for creating a log entry
# class LogCreate(LogBase):
#     pass

# # Model for updating a log entry with optional fields
# class LogUpdate(BaseModel):
#     log_type: Optional[str] = None
#     service_name: Optional[str] = None
#     level: Optional[str] = None
#     timestamp: Optional[datetime] = None
#     message: Optional[str] = None
#     metadata: Optional[Metadata] = None

# # Model for log response
# class LogResponse(LogBase):
#     # id: Optional[str] = Field(None, description="Log entry ID as a string")
#     service_name: Optional[str] = None


#     @classmethod
#     def from_mongo(cls, data: dict):
#         """Helper to convert MongoDB document to LogResponse format."""
#         if "_id" in data:
#             data["id"] = str(data["_id"])  # Convert ObjectId to string
#         return cls(**data)
