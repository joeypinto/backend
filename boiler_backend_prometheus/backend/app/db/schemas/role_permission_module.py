from typing import List, Optional
from pydantic import UUID4, BaseModel
from .permission import Permission
from .module import Module


# Shared properties
class RolePermissionBase(BaseModel):
    permission_id: int
    role_id: int
    module_id: int

# Properties to receive via API on creation
class RolePermissionCreate(RolePermissionBase):
    pass


# Properties to receive via API on update
class RolePermissionUpdate(BaseModel):
    permission_id: int
    module_id: int


class RolePermissionInDBBase(RolePermissionBase):
    #permission: Optional[Permission]
    #module: Optional[Module]

    class Config:
        orm_mode = True


# Additional properties to return via API
class RolePermission(RolePermissionInDBBase):
    pass


class RolePermissionInDB(RolePermissionInDBBase):
    pass
