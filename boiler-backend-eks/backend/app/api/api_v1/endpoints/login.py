from datetime import timedelta
from typing import Any
from app.tasks import send_recovery_password
from app.lib.util_mail import Email
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import repositories, models, schemas
from app.api import deps
from app.core import security
from app.core.config import settings
from app.core.security import get_password_hash
from app.utils import (
    generate_password_reset_token,
    verify_password_reset_token,
)

router = APIRouter()


@router.post("/login/access-token", response_model=schemas.Token)
async def login_access_token(
    *,
    db: AsyncSession = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests.
    """
    user = await repositories.user.authenticate(db,
                                                email=form_data.username,
                                                password=form_data.password
                                                )
    if not user:
        raise HTTPException(status_code=400, 
                            detail="Incorrect email or password")
    elif not repositories.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.
        create_access_token(user.id, expires_delta=access_token_expires),
        "token_type": "bearer",
        "user": user
    }


@router.post("/login/test-token", response_model=schemas.User)
async def test_token(current_user: models.User = Depends(deps.get_current_user)) -> Any:
    """
    Test access token.
    """
    return current_user


@router.post("/password-recovery/{email}", response_model=schemas.Msg)
async def recover_password(email: str,
                            db: AsyncSession = Depends(deps.get_db)
                        ) -> Any:
    """
    Password Recovery.
    """
    user = await repositories.user.get_by_email_or_username(db, email=email, username=email)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    # password_reset_token = generate_password_reset_token(email=email)

    token = generate_password_reset_token(email=email)
    #print('password_reset_token', token)
    #send_recovery_password.delay(token)
    await Email().sendVerificationCode(token=token)
    return {"msg": "Password recovery email sent"}


@router.post("/reset-password/", response_model=schemas.Msg)
async def reset_password(
    token: str = Body(...),
    new_password: str = Body(...),
    db: AsyncSession = Depends(deps.get_db),
) -> Any:
    """
    Reset password.
    """
    email = verify_password_reset_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = await repositories.user.get_by_email_or_username(db, email=email, username=email)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username or email does not exist in the system.",
        )
    elif not repositories.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    password = get_password_hash(new_password)
    user.password = password
    db.add(user)
    return {"msg": "Password updated successfully"}
