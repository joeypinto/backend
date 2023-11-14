from app.db.models.module import Module
from app.db.repositories.base import CRUDBase
from app.db.schemas.module import ModuleCreate, ModuleUpdate


class CRUDModule(CRUDBase[Module, ModuleCreate, ModuleUpdate]):
    pass

module = CRUDModule(Module)
