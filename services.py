import string
import random
from sqlmodel import Session, select
from model import UrlModel, ClickModel
from schemas import UrlCreate
from fastapi import Request
from datetime import datetime, timezone

def gerador_codigo(tamanho: int = 6) -> str:
    caracteres = string.ascii_letters + string.digits
    return "".join(random.choice(caracteres) for i in range(tamanho))

def criar_nova_url(session: Session, payload: UrlCreate) -> UrlCreate:
    codigo = gerador_codigo()

    nova_url = UrlModel(
        urlOriginal=payload.url_original,
        codigoGerado=codigo,
    )

    session.add(nova_url)
    session.commit()
    session.refresh(nova_url)

    return nova_url

def buscar_registrar_click(codigo: str, session: Session, request: Request) -> str | None:
    statment = select(UrlModel).where(UrlModel.codigoGerado == codigo)
    url_obj = session.exec(statment).first()

    if not url_obj:
        return None

    ip_cliente = request.client.host if request.client else "Desconhecido"

    novo_click = ClickModel(
        dataHora=datetime.now(timezone.utc),
        ip=ip_cliente,
        url_id=url_obj.id,
    )

    session.add(novo_click)
    session.commit()

    return url_obj.urlOriginal

def obter_analytics_url(codigo: str, session: Session) -> dict | None:
    statement = select(UrlModel).where(UrlModel.codigoGerado == codigo)
    url_obj = session.exec(statement).first()

    if not url_obj:
        return None

    clicks_statement = select(ClickModel).where(ClickModel.url_id == url_obj.id).order_by(ClickModel.dataHora.desc())
    clicks = session.exec(clicks_statement).all()

    return {
        "url_original": url_obj.urlOriginal,
        "codigo_gerado": url_obj.codigoGerado,
        "total_clicks": len(clicks),
        "ultimos_clicks": clicks
    }