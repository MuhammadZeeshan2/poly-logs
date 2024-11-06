# from pydantic import Field
# from pydantic_settings import BaseSettings

# from dotenv import load_dotenv
# import os


# load_dotenv()

# class Settings(BaseSettings):
#     # MongoDB connection fields
#     database_host: str = Field(..., env="DATABASE_HOST")
#     database_db: str = Field(..., env="DATABASE_DB")
#     database_user: str = Field(..., env="DATABASE_USER")
#     database_password: str = Field(..., env="DATABASE_PASSWORD")
#     database_port: int = Field(..., coerce_numbers_to_str=True)
#     @property
#     def mongodb_uri(self) -> str:
#         # MongoDB URI structure
#         return f"mongodb://{self.database_user}:{self.database_password}@{self.database_host}:{self.database_port}/{self.database_db}"

# urls = Settings()










# from pydantic import Field
# from pydantic_settings import BaseSettings

# from dotenv import load_dotenv
# import os


# load_dotenv()
# class Settings(BaseSettings):
#     database_host: str = Field(..., env="DATABASE_HOST")
#     database_db: str = Field(..., env="DATABASE_DB")
#     database_name: str = Field("postgres", env="DATABASE_USER")
#     database_password: str = Field("postgres", env="DATABASE_PASSWORD")
#     database_port: int = Field(5432, env="DATABASE_PORT")

#     @property
#     def _database_url(self):
#         return f"{self.database_host}:{self.database_port}"

#     @property
#     def postgres_database_conn_str(self) -> str:
#         return f"postgresql+asyncpg://{self.database_name}:{self.database_password}@{self._database_url}/{self.database_db}"


# urls = Settings()


# from pydantic import Field
# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     database_host: str = Field(..., env="DB_HOST")  # Updated to match .env
#     database_db: str = Field(..., env="DB_NAME")    # Updated to match .env
#     database_name: str = Field("postgres", env="DB_USERNAME")  # Updated to match .env
#     database_password: str = Field("postgres", env="DB_PASSWORD")  # Updated to match .env
#     database_port: int = Field(5432, env="DB_PORT")  # Updated to match .env

#     @property
#     def _database_url(self):
#         return f"{self.database_host}:{self.database_port}"

#     @property
#     def postgres_database_conn_str(self) -> str:
#         return f"postgresql+asyncpg://{self.database_name}:{self.database_password}@{self._database_url}/{self.database_db}"

# urls = Settings()
