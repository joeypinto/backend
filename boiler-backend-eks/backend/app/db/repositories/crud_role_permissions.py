from typing import Any, Optional
from .base import CRUDBase
from app.db.models.role_permission import RolePermission
from app.db.schemas.role_permission_module import RolePermissionCreate, RolePermissionUpdate  # noqa: E501, E261
from pydantic.types import UUID4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete


class CRUDRolePermission(CRUDBase[RolePermission, RolePermissionCreate, RolePermissionUpdate]):
    async def get_by_role_id(
        self, db: AsyncSession, *, role_id: int
    ) -> Optional[RolePermission]:
        stmt = select().where(self.model.role_id == role_id)
        result = await db.execute(stmt)
        return result.scalars().all()
    
    async def get_by_role(
        self, db: AsyncSession,
    ) -> Optional[RolePermission]:
        stmt = select(self.model)
        result = await db.execute(stmt)
        return result.scalars().all()


    async def remove_role(self, db: AsyncSession, *, role_id: Any) -> Optional[RolePermission]:
        stmt = delete(self.model).where(self.model.role_id == role_id)
        await db.execute(stmt)
        return await db.commit()


role_permission = CRUDRolePermission(RolePermission)
