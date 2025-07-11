from os import environ as env

from pydantic import BaseModel, Field


class DBConfig(BaseModel):
    user: str = Field(alias="POSTGRES_USER")
    password: str = Field(alias="POSTGRES_PASSWORD")
    host: str = Field(alias="POSTGRES_HOST")
    port: int = Field(alias="POSTGRES_PORT")
    database: str = Field(alias="POSTGRES_DB")
    echo: bool = False

    @property
    def uri(self) -> str:
        return f"postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


class Config(BaseModel):
    db: DBConfig = Field(default_factory=lambda: DBConfig(**env))


config: Config = Config()
