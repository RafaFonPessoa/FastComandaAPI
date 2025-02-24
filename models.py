from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from datetime import datetime

class Categories(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, nullable=False)
    categorie_name: str = Field(nullable=False)
    
    items: Optional[List["Items"]] = Relationship(back_populates="category")

class Items(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, nullable=False)
    name: str = Field(nullable=False)
    price : float = Field(nullable=False)
    categorie_id: int = Field(default=None, foreign_key="categories.id", nullable=False)
    
    category: "Categories" = Relationship(back_populates="items")

class Check(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    data: datetime = Field(default_factory=datetime.now)
    total: float = Field(default=0.0)
    
    itens: List["Items"] = Relationship(back_populates="comanda")