from http.client import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import repositories, schemas
from app.api import deps
from typing import Any, List
import logging

router = APIRouter()

LOGGER = logging.getLogger(__name__)


@router.post("/", response_model=schemas.Role)
async def create_role(
    *,
    db: AsyncSession = Depends(deps.get_db),
    role_in: schemas.RoleCreate,
) -> Any:
    """
    Create new role.
    """
    roles = await repositories.role.create(db, obj_in=role_in)
    return roles


@router.get("/", response_model=List[schemas.Role])
async def get_roles(
    db: AsyncSession = Depends(deps.get_db), skip: int = 0, limit: int = 100,
) -> Any:
    """
    Retrieve all available user roles.
    """
    LOGGER.info("Acess roles")
    roles = await repositories.role.get_multi(db=db, skip=skip, limit=limit)
    return roles


@router.put("/{id}", response_model=schemas.Role)
async def update_role(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: str,
    role_in: schemas.RoleUpdate,
) -> Any:
    """
    Update a role.
    """
    role = await repositories.role.get(db, id=id)
    if not role:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    role = await repositories.role.update(db, db_obj=role, obj_in=role_in)
    return role


@router.delete("/{id}", response_model=schemas.Role)
async def delete_roles(
    db: AsyncSession = Depends(deps.get_db), *, id: str,
) -> Any:
    """
    Delete a role.
    """
    roles = await repositories.role.remove(db=db, id=id)
    return roles

