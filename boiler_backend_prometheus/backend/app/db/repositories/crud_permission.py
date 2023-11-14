from app.db.models.permission import Permission
from app.db.repositories.base import CRUDBase
from app.db.schemas import PermissionCreate, PermissionUpdate
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDPermission(CRUDBase[Permission, PermissionCreate, PermissionUpdate]):
    pass


permission = CRUDPermission(Permission)
