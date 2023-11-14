from http.client import HTTPException
from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import repositories, schemas
from app.api import deps


router = APIRouter()


@router.post("/", response_model=schemas.Permission)
async def create_permission(
    *,
    db: AsyncSession = Depends(deps.get_db),
    permission_in: schemas.PermissionCreate,
) -> Any:
    """
    Create new permission.
    """
    permission = await repositories.permission.create(db, obj_in=permission_in)
    return permission


@router.get("/", response_model=List[schemas.Permission])
async def get_permissions(
    db: AsyncSession = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
) -> Any:
    """
    Retrieve all available permissions.
    """
    permissions = await repositories.permission.get_multi(db=db, skip=skip, limit=limit)
    return permissions


@router.delete("/{id}", response_model=schemas.Permission)
async def delete_permission(
    db: AsyncSession = Depends(deps.get_db), *, id: str,
) -> Any:
    """
    Delete a permission.
    """
    permission = await repositories.permission.remove(db=db, id=id)
    return permission


@router.put("/{id}", response_model=schemas.Permission)
async def update_permission(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: str,
    permission_in: schemas.PermissionUpdate,
) -> Any:
    """
    Update a permission.
    """
    permission = await repositories.permission.get(db, id=id)
    if not permission:
        raise HTTPException(
            status_code=404,
            detail="The permission with this id does not exist in the system",
        )
    permission = await repositories.permission.update(db, db_obj=permission, obj_in=permission_in)
    return permission
