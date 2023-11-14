from typing import Optional
from app.db.schemas.module import Module
from pydantic import UUID4, BaseModel


# Shared properties
class PermissionBase(BaseModel):
    name: Optional[str]
    description: Optional[str]
    


# Properties to receive via API on creation
class PermissionCreate(PermissionBase):
    module_id: Optional[int]
    pass


# Properties to receive via API on update
class PermissionUpdate(PermissionBase):
    module_id: Optional[int]


class PermissionInDBBase(PermissionBase):
    id: int
    #module: Optional[Module]

    class Config:
        orm_mode = True


# Additional properties to return via API
class Permission(PermissionInDBBase):
    pass


class PermissionInDB(PermissionInDBBase):
    pass
