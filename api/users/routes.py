from fastapi import APIRouter, Depends, HTTPException, status
from api.schemas import ResourceCreatedResponse, ResourceDeletedResponse, UserSchema, LogResponse, LogListResponse
from api.users.services import UserService

from typing import List
from bson import ObjectId

# Initialize routers
user_router = APIRouter()
user_service = UserService()


# User endpoints
@user_router.get("/", tags=["Users"], response_model=List[UserSchema], status_code=status.HTTP_200_OK)
async def get_all_users():
    return await user_service.list_users()

@user_router.get("/{user_id}", tags=["Users"], response_model=UserSchema, status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: str):
    try:
        user = await user_service.get_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.post("/", tags=["Users"], response_model=ResourceCreatedResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserSchema):
    if await user_service.user_exists(username=user.username, email=user.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email already exists"
        )
    user_id = await user_service.create_user(user.dict(exclude_unset=True))
    return ResourceCreatedResponse(detail="User created successfully", id=user_id)

@user_router.put("/{user_id}", tags=["Users"], response_model=UserSchema, status_code=status.HTTP_200_OK)
async def update_user(user_id: str, user: UserSchema):
    if not await user_service.update_user(user_id, user.dict(exclude_unset=True)):
        raise HTTPException(status_code=404, detail="User not found or update failed")
    return await user_service.get_user(user_id)

@user_router.delete("/{user_id}", tags=["Users"], response_model=ResourceDeletedResponse, status_code=status.HTTP_200_OK)
async def delete_user(user_id: str):
    if not await user_service.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return ResourceDeletedResponse(detail="User deleted successfully")

# Log endpoints

# from fastapi import APIRouter, Depends, status

# from api.constants import ErrorCodes
# from api.exceptions import ObjectNotFoundException, UniqueKeyViolationException
# from api.schemas import ResourceCreatedResponse, ResourceDeletedResponse
# from api.users.dependencies import get_user_service
# from api.users.schemas import InUserSchema, InUserUpdateSchema, OutUserSchema, OutUsersSchema
# from api.users.services import UserService

# from logger import logger

# router = APIRouter()

# # ... (other imports remain the same)

# @router.get("/", tags=["Get all users"], response_model=list[OutUsersSchema], status_code=status.HTTP_200_OK)
# async def get_all_users(user_service: UserService = Depends(get_user_service)) -> list[OutUsersSchema]:
#     logger.debug(f"Get all users endpoint hit")
#     return await user_service.list()  # Add await here

# @router.get("/{id}", tags=["Get user by id"], response_model=OutUserSchema, status_code=status.HTTP_200_OK)
# async def get_user_by_id(id: int, user_service: UserService = Depends(get_user_service)) -> OutUserSchema:
#     logger.info(f"Fetching user with id {id}")
#     try:
#         user = await user_service.get(id=id)  # Add await here
#     except ObjectNotFoundException as e:
#         logger.debug(f"User with id {id} not found. Throwing 404 Not Found error")
#         e.detail = ErrorCodes.USER_NOT_FOUND
#         raise e
#     return user

# @router.post("/", tags=["Create user"], response_model=ResourceCreatedResponse, status_code=status.HTTP_201_CREATED)
# async def create_user(user: InUserSchema, user_service: UserService = Depends(get_user_service)):
#     if await user_service.user_exists(username=user.username, email=user.email):  # Add await here
#         logger.debug(
#             f"User with this username {user.username} or email {user.email} already exists. "
#             f"Throwing 409 Conflict error"
#         )
#         raise UniqueKeyViolationException(
#             status_code=status.HTTP_409_CONFLICT, detail=ErrorCodes.USERNAME_OR_EMAIL_ALREADY_EXISTS
#         )
#     new_user = await user_service.create(user)  # Add await here
#     logger.info(f"User created with id: {new_user.id}")
#     return ResourceCreatedResponse(detail="User created successfully", id=new_user.id)

# @router.put(
#     "/{id}",
#     tags=["Update user"],
#     response_model=OutUserSchema | ResourceDeletedResponse,
#     status_code=status.HTTP_200_OK,
# )
# async def update_user(id: int, user: InUserUpdateSchema, user_service: UserService = Depends(get_user_service)):
#     if user.is_deleted:
#         await user_service.delete(id=id)  # Add await here
#         logger.info(f"User with id {id} deleted")
#         return ResourceDeletedResponse(detail="User deleted successfully", id=id)
#     else:
#         try:
#             await user_service.update(id=id, obj=user)  # Add await here
#         except UniqueKeyViolationException as e:
#             logger.debug(
#                 f"User with this username {user.username} or email {user.email} already exists. "
#                 f"Throwing 409 Conflict error"
#             )
#             e.detail = ErrorCodes.USERNAME_OR_EMAIL_ALREADY_EXISTS
#             raise e
#         except ObjectNotFoundException as e:
#             logger.debug(f"User with id {id} not found. Throwing 404 Not Found error")
#             e.detail = ErrorCodes.USER_NOT_FOUND
#             raise e
#         logger.info(f"User with id {id} updated")
#         return await user_service.get(id=id)  # Add await here
