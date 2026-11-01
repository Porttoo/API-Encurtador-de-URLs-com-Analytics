from pydantic import BaseModel
from datetime import datetime

class UrlCreate(BaseModel):
    url_original: str

class ClickInfo(BaseModel):
    dataHora: datetime
    ip: str

    class Config:
        from_attributes = True

class UrlAnalyticsResponse(BaseModel):
    url_original: str
    codigo_gerado: str
    total_clicks: int
    ultimos_clicks: list[ClickInfo]

    class Config:
        from_attributes = True