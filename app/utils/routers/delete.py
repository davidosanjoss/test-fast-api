import uuid

from app.configs import db_session

from .default import RoutersParams


class RoutersDelete(RoutersParams):
    def delete(self):
        ModelIn = self.model_in
        ModelOut = self.model_out

        @self.router.delete("/{id}", response_model=ModelOut)
        async def delete_id(id: uuid.UUID, data: ModelIn, session: db_session):
            self.session = session
            instance = self.get_model(id)

            update_data = data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(instance, key, value)

            await self.save(instance, refresh=False)

            return instance
