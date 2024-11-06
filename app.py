# Main app setup
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from api.users.routes import  user_router
from api.logs.routes import log_router
from database import client
from logger import logger

app = FastAPI(
    title="ISSM FastAPI Template",
    description="This is a very fancy project, with auto docs for the API and everything."
)

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    logger.info(f"{request.method} {request.url.path} - status {response.status_code}")
    return response

# Include the routers with consistent prefixes and tags
# app.include_router(user_router, prefix="/api/v1/users", tags=["Users"])
app.include_router(log_router, prefix="/api/v1/logs", tags=["Logs"])

@app.on_event("startup")
async def startup_event():
    logger.info("Application started")
    try:
        await client.admin.command("ping")  # MongoDB test command
        logger.info("Connected to MongoDB successfully")
    except Exception as e:
        logger.error("Failed to connect to MongoDB", exc_info=e)

@app.get("/",tags=["Root"])
async def read_root():
    logger.info("Root endpoint hit")
    return {"message": "Welcome to ISSM FastAPI Template"}











# from fastapi import FastAPI, Request, status
# from fastapi.middleware.cors import CORSMiddleware

# from api.users.routes import router as users_router
# from database import client  # Import the MongoDB client instead
# from logger import logger

# app = FastAPI(
#     title="ISSM Fastapi Template",
#     description="This is a very fancy project, with auto docs for the API and everything."
# )
# app.add_middleware(
#     CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
# )

# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     response = await call_next(request)
#     logger.info(f"{request.method} {request.url.path} - status {response.status_code}")
#     return response

# app.include_router(users_router, prefix="/api/v1/users", tags=["Users"])

# @app.on_event("startup")
# async def startup_event():
#     logger.info("Application started")
#     # MongoDB client is automatically connected, so no need for create_database
#     # Can check if the connection works, though:
#     try:
#         await client.admin.command("ping")  # MongoDB test command
#         logger.info("Connected to MongoDB successfully")
#     except Exception as e:
#         logger.error("Failed to connect to MongoDB", exc_info=e)

# @app.get("/")
# async def read_root():
#     logger.info("Root endpoint hit")
#     return status.HTTP_200_OK








#from fastapi import FastAPI, Request, status
# from fastapi.middleware.cors import CORSMiddleware

# from api.users.routes import router as users_router
# from database import db_object

# from logger import logger

# app = FastAPI(
#     title="ISSM Fastapi Template",
#     description="""This is a very fancy project, with auto docs for the API and everything.""",
# )
# app.add_middleware(
#     CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
# )


# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     response = await call_next(request)
#     logger.info(f"{request.method} {request.url.path} - status {response.status_code}")
#     return response


# app.include_router(users_router, prefix="/api/v1/users", tags=["Users"])


# # TODO: Setup global timestamp for all output models (schemas-pydantic)

# @app.on_event("startup")
# async def startup_event():
#     logger.info("Application started")
#     await db_object.create_database()


# @app.get("/")
# async def read_root():
#     logger.info("Root endpoint hit")
#     return status.HTTP_200_OK
 