from typing import Optional

from app.db.schemas.role import Role # noqa: F401, E261 
from pydantic import UUID4, BaseModel


# Shared properties
class UserRoleBase(BaseModel):
    user_id: Optional[int]
    role_id: Optional[int]


# Properties to receive via API on creation
class UserRoleCreate(UserRoleBase):
    pass


# Properties to receive via API on update
class UserRoleUpdate(BaseModel):
    role_id: int


class UserRoleInDBBase(UserRoleBase):
    roles: Optional[Role]

    class Config:
        orm_mode = True


# Additional properties to return via API
class UserRole(UserRoleInDBBase):
    pass


class UserRoleInDB(UserRoleInDBBase):
    pass
