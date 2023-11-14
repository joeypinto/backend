from http.client import HTTPException
from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import repositories, schemas
from app.api import deps


router = APIRouter()


@router.post("/", response_model=schemas.Module)
async def create_module(
    *,
    db: AsyncSession = Depends(deps.get_db),
    module_in: schemas.ModuleCreate,
) -> Any:
    """
    Create new module.
    """
    module = await repositories.module.create(db, obj_in=module_in)
    return module


@router.get("/", response_model=List[schemas.Module])
async def get_modules(
    db: AsyncSession = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
) -> Any:
    """
    Retrieve all available modules.
    """
    modules = await repositories.module.get_multi(db=db, skip=skip, limit=limit)
    return modules


@router.delete("/{id}", response_model=schemas.Module)
async def delete_module(
    db: AsyncSession = Depends(deps.get_db), *, id: str,
) -> Any:
    """
    Delete a module.
    """
    module = await repositories.module.remove(db=db, id=id)
    return module


@router.put("/{id}", response_model=schemas.Module)
async def update_module(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: str,
    module_in: schemas.ModuleUpdate,
) -> Any:
    """
    Update a module.
    """
    module = await repositories.module.get(db, id=id)
    if not module:
        raise HTTPException(
            status_code=404,
            detail="The module with this id does not exist in the system",
        )
    module = await repositories.module.update(db, db_obj=module, obj_in=module_in)
    return module
