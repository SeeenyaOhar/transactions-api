from datetime import datetime

from typing import Optional
from typing import List

from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import validates
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey

from .validators import EmailValidator
from .validators import NameValidator


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(16), nullable=False)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    surname: Mapped[str] = mapped_column(String(30), nullable=False)
    
    transactions: Mapped[List["Transaction"]] = relationship(back_populates="user")
    _email_validator = EmailValidator()
    _name_validator = NameValidator()

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, surname={self.surname!r})"

    @validates('email')
    def validate_email(self, key, value):
        return self._email_validator.validate(value)

    @validates('name')
    def validate_name(self, key, value):
        return self._name_validator.validate(value)

    @validates('surname')
    def validate_name(self, key, value):
        return self._name_validator.validate(value)


class Transaction(Base):
    __tablename__ = "transaction"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[int] = mapped_column(nullable=False)
    date: Mapped[datetime] = mapped_column(nullable=False)
    category: Mapped[str] = mapped_column(nullable=False) 
    tag: Mapped[Optional[str]] = mapped_column(String(30))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="transactions")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self) -> str:
        return f"Transaction(id={self.id!r}, amount={self.amount!r}, " \
            + f"date={self.date!r}), category={self.category.name!r}, tag={self.tag!r}, user={self.user.email!r}"
