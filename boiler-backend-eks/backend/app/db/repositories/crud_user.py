from ast import List
import datetime
from app.db.models.user_role import UserRole
from app.db.models.role import Role
from sqlalchemy import or_
from typing import Any, Dict, Optional, Union
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import get_password_hash, verify_password
from app.db.repositories.base import CRUDBase
from app.db.models.user import User
from app.db.schemas.user import UserCreate, UserUpdate
from app.db.schemas.role import RoleBase

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    async def get_by_email_or_username(self, db: AsyncSession, *,
                           email: str, username: str) -> Optional[User]:
        stmt = select(self.model).where(or_(self.model.email == email, self.model.username == username))
        result = await db.execute(stmt)
        return result.scalars().first()

    async def create_open_user(self, db: AsyncSession, *, obj_in: UserCreate) -> User:

        new_user = User(
            email=obj_in.email,
            password=get_password_hash(obj_in.password),
            username=obj_in.username,     
        )
        db.add(new_user)   
        await db.commit()
        await db.refresh(new_user)
        return new_user

    async def update(self, db: AsyncSession, *, db_obj: User,
                     obj_in: Union[UserUpdate, Dict[str, Any]]) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["password"] = password
        return await super().update(db, db_obj=db_obj, obj_in=update_data)

    async def authenticate(self, db: AsyncSession, *,
                           email: str, password: str) -> Optional[User]:
        user = await self.get_by_email_or_username(db, email=email, username=email)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active


user = CRUDUser(User)
