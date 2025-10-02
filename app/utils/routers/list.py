import uuid

from typing import Annotated, List
from fastapi import HTTPException, Query
from sqlmodel import select

from app.configs.database import SessionDep
from .default import RoutersParams


class RoutersList(RoutersParams):
    def list_many(self):
        Model = self.model
        ModelOut = self.model_out

        @self.router.get("/", response_model=List[ModelOut])
        async def read_many(
                session: SessionDep,
                offset: int = 0,
                limit: Annotated[int, Query(le=100)] = 100,
        ):
            self.session = session
            result = await session.execute(select(Model).offset(offset).limit(limit))
            return result.scalars().all()

    def list_one(self):
        Model = self.model
        ModelOut = self.model_out

        @self.router.get("/{id}/", response_model=ModelOut)
        async def read_id(id: uuid.UUID, session: SessionDep):
            self.session = session
            instance = await session.get(Model, id)
            if not instance:
                raise HTTPException(
                    status_code=404, detail=f"{Model.__name__} not found"
                )
            return instance

    def list_choices(self):
        Model = self.model
        ModelOut = self.model_out

        @self.router.get("/choices/", response_model=List[ModelOut])
        async def read_choices(session: SessionDep):
            self.session = session
            result = await self.session.execute(select(Model))
            return result.scalars().all()
