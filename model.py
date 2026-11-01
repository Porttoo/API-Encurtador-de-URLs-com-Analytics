from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class UrlModel(SQLModel, table=True):
    __tablename__ = "urls"
    id: Optional[int] = Field(default=None, primary_key=True)
    urlOriginal: str = Field(nullable=False)
    codigoGerado: str = Field(unique=True, index=True)

class ClickModel(SQLModel, table=True):
    __tablename__ = "clicks"
    id: Optional[int] = Field(default=None, primary_key=True)
    dataHora: datetime = Field(default_factory=datetime.now)
    ip: str = Field(index=True, max_length=15)
    url_id: int = Field(foreign_key="urls.id")