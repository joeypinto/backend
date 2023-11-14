from typing import List, Optional
from app.db.repositories.base import CRUDBase
from app.db.models.role import Role
from app.db.schemas.role import RoleCreate, RoleUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import UUID
from app.db.models.user import User
from sqlalchemy import select


class CRUDRole(CRUDBase[Role, RoleCreate, RoleUpdate]):
    async def get_role_by_name(self, db: AsyncSession,
                               *, name: str) -> Optional[Role]:
        async with db as session:
            return await session(self.model).filter(Role.name == name).first()

    # async def get(self, db: AsyncSession, *, skip: int,
    #               limit: int) -> List[Role]:
    #     print(skip, limit)
    #     async with db as session:
    #         stmt = select(self.model).offset(10).limit(100)
    #         result = await session.execute(stmt)
    #         print(result)
    #         return result.scalars().all()

    async def add_role_to_user(self, db: AsyncSession, *,
                               role_id: UUID, user: User) -> Optional[Role]:
        role = await super().get(id=role_id)
        role.users.append(user)
        db.session.add(role)
        await db.session.commit()
        await db.session.refresh(role)
        return role


role = CRUDRole(Role)
