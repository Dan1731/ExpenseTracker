from datetime import datetime
from decimal import Decimal
from typing import List, Annotated, Optional
from sqlalchemy import ForeignKey, String, Numeric, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Local imports
from init_extension import db

class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True) # auto-increments
    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(50), nullable=False)
    creation_time: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    # one-to-many relationship to expense_transactions
    expenses: Mapped[List["ExpenseTrans"]] = relationship(back_populates="creator")
    
    # one-to-many relationship to expense_categories
    categories: Mapped[List["ExpenseCat"]] = relationship(back_populates="creator")

class ExpenseTrans(db.Model):
    __tablename__ = "expense_trans"

    id: Mapped[int] = mapped_column(primary_key=True) # auto-increments
    amount: Mapped[Decimal] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("expense_cats.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    expense_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)

     # many-to-one relationship to users
    creator: Mapped["User"] = relationship(back_populates="expenses")

    # many-to-one relationship to expense_categories
    category: Mapped["ExpenseCat"] = relationship(back_populates="transactions")

class ExpenseCat(db.Model):
    __tablename__ = "expense_cats"

    id: Mapped[int] = mapped_column(primary_key=True) # auto-increments
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)

    # many-to-one relationship to users
    creator: Mapped["User"] = relationship(back_populates="categories")

    # one-to-many relationship to expense_transactions
    transactions: Mapped[List["ExpenseTrans"]] = relationship(back_populates="category")

