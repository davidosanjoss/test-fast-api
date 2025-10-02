from fastapi import APIRouter, Depends

from app.utils.routers import Routers
from app.configs.database import get_session
from ..schemas.users import Users, UserOut, UserIn

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_session)],
    responses={404: {"description": "Not found"}},
)


class UserRouter(Routers):
    router = router
    model = Users
    model_in = UserIn
    model_out = UserOut


UserRouter().add_all_routers(use_choices=False)
