import uuid

from .default import RoutersParams
from app.configs.database import SessionDep


class RoutersUpdate(RoutersParams):
    def update(self):
        ModelIn = self.model_in
        ModelOut = self.model_out

        @self.router.patch("/{id}", response_model=ModelOut)
        async def update_id(id: uuid.UUID, data: ModelIn, session: SessionDep):
            self.session = session

            instance = self.get_model(id)

            update_data = data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(instance, key, value)

            await self.save(instance)

            return instance
