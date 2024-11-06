from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_host: str
    database_user: str
    database_password: str
    database_port: int
    log_to_file: bool
    log_to_console: bool
    log_level: str
    log_file_path: str

    class Config:
        env_file = ".env"
        extra = "allow"  

config = Settings()


# from pydantic import Field
# from pydantic_settings import BaseSettings
# from dotenv import load_dotenv
# import os 
# load_dotenv()
# print(os.environ)
# class Settings(BaseSettings):
#     # MongoDB connection fields
#     database_host: str = Field(..., env="DATABASE_HOST")
#     database_db: str = Field(..., env="DATABASE_DB")
#     database_user: str = Field(..., env="DATABASE_USER")
#     database_password: str = Field(..., env="DATABASE_PASSWORD")
#     database_port: int = Field(..., coerce_numbers_to_str=True)

#     # Logger Configuration
#     log_to_file: bool = Field(True, env="LOG_TO_FILE")
#     log_to_console: bool = Field(True, env="LOG_TO_CONSOLE")
#     log_level: str = Field("INFO", env="LOG_LEVEL")
#     log_file_path: str = Field("logs", env="LOG_FILE_PATH")

#     @property
#     def _database_url(self):
#         return f"{self.database_host}:{self.database_port}"

#     @property
#     def mongodb_uri(self) -> str:
#         return f"mongodb://{self.database_user}:{self.database_password}@{self.database_host}:{self.database_port}/{self.database_db}"

# # Instantiate the Settings
# config = Settings()

# from pydantic import Field
# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     # Logger Configuration
#     log_to_file: bool = Field(True, env="LOG_TO_FILE")
#     log_to_console: bool = Field(True, env="LOG_TO_CONSOLE")
#     log_level: str = Field("DEBUG", env="LOG_LEVEL")  # Use 'DEBUG' for consistency
#     log_file_path: str = Field("logs", env="LOG_FILE_PATH")

#     # Database Configuration
#     database_host: str = Field(..., env="DB_HOST")
#     database_db: str = Field(..., env="DB_NAME")
#     database_name: str = Field("postgres", env="DB_USERNAME")
#     database_password: str = Field("postgres", env="DB_PASSWORD")
#     database_port: int = Field(5432, env="DB_PORT")

#     @property
#     def _database_url(self):
#         return f"{self.database_host}:{self.database_port}"

#     @property
#     def postgres_database_conn_str(self) -> str:
#         return f"postgresql+asyncpg://{self.database_name}:{self.database_password}@{self._database_url}/{self.database_db}"

# # Instantiate the Settings
# config = Settings()
