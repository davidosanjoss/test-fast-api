from app.configs.database import SessionDep

from .default import RoutersParams


class RoutersCreate(RoutersParams):
    def create(self):
        Model = self.model
        ModelIn = self.model_in
        ModelOut = self.model_out

        @self.router.post("/", response_model=ModelOut)
        async def create(data: ModelIn, session: SessionDep):
            self.session = session
            instance = await Model(**data.model_dump())

            await self.save(instance)

            return instance
