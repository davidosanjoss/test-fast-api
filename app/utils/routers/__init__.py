from .create import RoutersCreate
from .delete import RoutersDelete
from .list import RoutersList
from .update import RoutersUpdate


class Routers(RoutersList, RoutersCreate, RoutersUpdate, RoutersDelete):

    def add_all_routers(self, **kwargs):
        self.list_many()
        self.list_one()
        if kwargs.get("use_choices"):
            self.list_choices()
        self.create()
        self.update()
        self.delete()
