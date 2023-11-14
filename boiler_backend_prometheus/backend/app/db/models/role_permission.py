from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, UniqueConstraint, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.models.permission import Permission
from app.db.models.role import Role
from app.db.models.module import Module


class RolePermission(Base):
    __tablename__ = "role_permission"
    id = Column(
        Integer, primary_key=True, index=True
    )
    role_id = Column(
        Integer,
        ForeignKey("role.id", onupdate='CASCADE', ondelete='SET NULL'),
        primary_key=True,
        nullable=False,
    )
    permission_id = Column(
        Integer,
        ForeignKey("permission.id"),
        primary_key=True,
        nullable=False,
    )
    role = relationship("Role", lazy="selectin")
    permission = relationship("Permission", lazy="selectin")

    __table_args__ = (
        UniqueConstraint("role_id", "permission_id",
                        name="unique_role_permission"),
    )

