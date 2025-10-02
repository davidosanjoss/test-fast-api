import uuid
from datetime import date, datetime

from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from app.utils.models import ModelBase


class Users(ModelBase, table=True):
    username: str = Field(max_length=100, index=True)
    email: EmailStr = Field(max_length=100, unique=True, index=True)
    birthday: date | None = Field(default=None)
    password: str


class UserIn(SQLModel):
    username: str = Field(max_length=100, index=True)
    email: EmailStr = Field(max_length=100, unique=True, index=True)
    password: str


class UserOut(SQLModel):
    id: uuid.UUID
    username: str = Field(max_length=100, index=True)
    email: EmailStr = Field(max_length=100, unique=True, index=True)
    birthday: date | None = Field(default=None)
    password: str
    created_at: datetime
    updated_at: datetime
