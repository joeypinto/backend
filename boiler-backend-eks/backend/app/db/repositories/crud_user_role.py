from typing import Optional
from app.db.repositories.base import CRUDBase
from app.db.models.user_role import UserRole
from app.db.schemas.user_role import UserRoleCreate, UserRoleUpdate
from pydantic.types import UUID4
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDUserRole(CRUDBase[UserRole, UserRoleCreate, UserRoleUpdate]):
    async def get_by_user_id(
        self, db: AsyncSession, *, user_id: UUID4
    ) -> Optional[UserRole]:
        async with db as session:
            return await session(UserRole).filter(
                UserRole.user_id == user_id).first()


user_role = CRUDUserRole(UserRole)
