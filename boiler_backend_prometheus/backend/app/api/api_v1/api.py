
from fastapi import APIRouter
from app.api.api_v1.endpoints import login, users, permissions, modules, role

api_router = APIRouter()

api_router.include_router(login.router, tags=["login"])

api_router.include_router(users.router, prefix="/users", tags=["users"])

api_router.include_router(permissions.router, prefix="/permissions", tags=["permissions"])

api_router.include_router(modules.router, prefix="/modules", tags=["modules"])

api_router.include_router(role.router, prefix="/roles", tags=["roles"])