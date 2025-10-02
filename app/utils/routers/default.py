import uuid
from http.client import HTTPException
from typing import Annotated, Type
from fastapi import APIRouter, Depends
from sqlmodel import SQLModel

from sqlalchemy.ext.asyncio import AsyncSession
from app.configs.database import get_session


class RoutersParams:
    router: APIRouter
    model: Type[SQLModel]
    model_in: Type[SQLModel]
    model_out: Type[SQLModel]
    session: Annotated[AsyncSession, Depends(get_session)]

    def __init__(self):
        if not self.router or not self.model or not self.model_in or not self.model_out:
            raise Exception(
                "You must define router, model, model_in and model_out in your subclass"
            )

    async def get_model(self, id: uuid.UUID):
        instance = await self.session.get(self.model, id)
        if not instance:
            raise HTTPException(
                status_code=404, detail=f"{self.model.__name__} not found"
            )

        return instance

    async def save(self, instance, **kwargs):
        self.session.add(instance)
        await self.session.commit()

        if kwargs.get("refresh", True):
            await self.session.refresh(instance)
