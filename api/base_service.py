from typing import Generic, Optional, Type, TypeVar
from pydantic import BaseModel
from api.exceptions import ObjectNotFoundException, UniqueKeyViolationException
from database import db
from database.models import LogBase, LogCreate, LogUpdate
from bson import ObjectId

# Generic type variables for base service
ModelType = TypeVar("ModelType", bound=LogBase)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, collection_name: str):
        self.collection = db[collection_name]  # Use the provided collection name

    async def get(self, id: str) -> Optional[ModelType]:
        document = await self.collection.find_one({"_id": ObjectId(id)})
        if document is None:
            raise ObjectNotFoundException(status_code=404, detail="Not Found")
        document["_id"] = str(document["_id"])  # Convert ObjectId to str
        return document

    async def list(self, limit: int = 10, skip: int = 0) -> list[ModelType]:
        cursor = self.collection.find().skip(skip).limit(limit)
        documents = await cursor.to_list(length=limit)
        for doc in documents:
            doc["_id"] = str(doc["_id"])  # Convert ObjectId to str
        return documents

    async def create(self, obj: CreateSchemaType) -> str:
        log_data = obj.dict()
        result = await self.collection.insert_one(log_data)
        return str(result.inserted_id)

    async def update(self, id: str, obj: UpdateSchemaType) -> Optional[ModelType]:
        update_data = obj.dict(exclude_unset=True)
        result = await self.collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
        
        if result.matched_count == 0:
            raise ObjectNotFoundException(status_code=404, detail="Not Found")
        
        return await self.get(id)  # Return the updated document

    async def delete(self, id: str) -> None:
        result = await self.collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            raise ObjectNotFoundException(status_code=404, detail="Not Found")








# from typing import Generic, Optional, Type, TypeVar
# from sqlalchemy import select
# from sqlalchemy.exc import IntegrityError
# from pydantic import BaseModel
# from api.exceptions import ObjectNotFoundException, UniqueKeyViolationException
# # from database import Base
# from database import db
# from database.models import LogBase, LogCreate, LogUpdate
# from bson import ObjectId
# ModelType = TypeVar("ModelType", bound=Base)
# CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
# UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

# # class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
# #     def __init__(self, model: Type[ModelType], db_object):
# #         self.model = model
# #         self.db_object = db_object

# #     async def get(self, id: int) -> Optional[ModelType]:
# #         async with self.db_object.db() as session:  # db() here is an async context manager
# #             stmt = select(self.model).where(self.model.id == id, self.model.is_deleted == False)
# #             result = await session.execute(stmt)
# #             obj = result.scalar_one_or_none()
# #             if obj is None:
# #                 raise ObjectNotFoundException(status_code=404, detail="Not Found")
# #             return obj

# #     async def list(self) -> list[ModelType]:
# #         async with self.db_object.db() as session:
# #             stmt = select(self.model).where(self.model.is_deleted == False)
# #             result = await session.execute(stmt)
# #             return result.scalars().all()

# #     async def create(self, obj: CreateSchemaType) -> ModelType:
# #         async with self.db_object.db() as session:
# #             db_obj: ModelType = self.model(**obj.dict())
# #             session.add(db_obj)
# #             try:
# #                 await session.commit()
# #             except IntegrityError as e:
# #                 await session.rollback()
# #                 if "duplicate key" in str(e):
# #                     raise UniqueKeyViolationException(status_code=409, detail="Conflict Error")
# #                 else:
# #                     raise e
# #             return db_obj

# #     async def update(self, id: int, obj: UpdateSchemaType) -> Optional[ModelType]:
# #         async with self.db_object.db() as session:
# #             db_obj = await self.get(id)
# #             update_data = obj.model_dump(exclude_unset=True)
# #             for column, value in update_data.items():
# #                 setattr(db_obj, column, value)
# #             try:
# #                 session.add(db_obj)
# #                 await session.commit()
# #             except IntegrityError as e:
# #                 await session.rollback()
# #                 if "duplicate key" in str(e):
# #                     raise UniqueKeyViolationException(status_code=409, detail="Conflict Error")
# #                 else:
# #                     raise e
# #             return db_obj

# #     async def delete(self, id: int) -> None:
# #         async with self.db_object.db() as session:
# #             db_obj = await self.get(id)
# #             db_obj.is_deleted = True
# #             session.add(db_obj)
# #             try:
# #                 await session.commit()
# #             except IntegrityError as e:
# #                 await session.rollback()
# #                 if "duplicate key" in str(e):
# #                     raise UniqueKeyViolationException(status_code=409, detail="Conflict Error")
# #                 else:
# #                     raise e

