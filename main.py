from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlmodel import Session
from database import init_db, engine
from schemas import UrlCreate, UrlAnalyticsResponse
from services import criar_nova_url, buscar_registrar_click, obter_analytics_url

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

def get_session():
    with Session(engine) as session:
        yield session

@app.get("/")
def home():
    return {"mensagem": "API Encurtador de URLs com Analytics Online"}

@app.post("/encurtador")
def encurtador(payload: UrlCreate, session: Session = Depends(get_session)):
    nova_url = criar_nova_url(session, payload)

    return {"mensagem": "URL encurtada com sucesso",
            "url_original": nova_url.urlOriginal,
            "codigoGerado": nova_url.codigoGerado,
            "link_curto": f"http://localhost:8000/{nova_url.codigoGerado}"
    }

@app.get("/{codigo}")
def redirecionar(codigo: str, request: Request, session: Session = Depends(get_session)):
    url_original = buscar_registrar_click(codigo, session, request)

    if not url_original:
        raise HTTPException(status_code=404, detail="Link encurtado não encontrado",)

    return RedirectResponse(url=url_original, status_code=307)

@app.get("/analytics/{codigo}", response_model=UrlAnalyticsResponse)
def obter_analytics(codigo: str, session: Session = Depends(get_session)):
    analytics = obter_analytics_url(codigo, session)

    if not analytics:
        raise HTTPException(status_code=404, detail="Link não encontrado para analytics")

    return analytics