from pydantic import UUID4, BaseModel
from typing import List, Optional # noqa: F401, E261
from datetime import datetime # noqa: F401, E261
#from app.db.schemas.role_permission_module import RolePermission


# Shared properties
class RoleBase(BaseModel):
    name: Optional[str]
    description: Optional[str]


# Properties to receive via API on creation
class RoleCreate(RoleBase):
    pass


# Properties to receive via API on update
class RoleUpdate(RoleBase):
    pass


class RoleInDBBase(RoleBase):
    id: int
    #created_at: Optional[datetime]
    #updated_at: Optional[datetime]
    #role_permission: Optional[List[RolePermission]]
    
    class Config:
        orm_mode = True


# Additional properties to return via API
class Role(RoleInDBBase):
    pass


class RoleInDB(RoleInDBBase):
    pass
