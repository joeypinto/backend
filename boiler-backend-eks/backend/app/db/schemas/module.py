from typing import Optional
from pydantic import UUID4, BaseModel


# Shared properties
class ModuleBase(BaseModel):
    name: Optional[str]
    description: Optional[str]
    


# Properties to receive via API on creation
class ModuleCreate(ModuleBase):
    pass


# Properties to receive via API on update
class ModuleUpdate(ModuleBase):
    name: Optional[str]
    description: Optional[str]


class ModuleInDBBase(ModuleBase):
    id: int
    permissions: Optional[list]
    class Config:
        orm_mode = True


# Additional properties to return via API
class Module(ModuleInDBBase):
    pass


class ModuleInDB(ModuleInDBBase):
    pass
