from sqlalchemy.orm import DeclarativeBase

from core.db.mixins.timestamp import TimestampMixin
from core.db.mixins.audit import AuditMixin


class Base(DeclarativeBase): ...


class BaseModel(Base, TimestampMixin, AuditMixin):
    __abstract__ = True
