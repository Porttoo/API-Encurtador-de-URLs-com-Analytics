import random
from datetime import datetime, timedelta, timezone
from sqlmodel import Session
from database import engine
from model import UrlModel, ClickModel
from faker import Faker

fake = Faker()

def popular_banco():
    with Session(engine) as session:
        print("Inserindo URLs e cliques simulados...")

        urls = [
            "https://github.com/Porttoo",
            "https://www.linkedin.com/in/gabrielrosaporto/",
            "https://fastapi.tiangolo.com",
            "https://www.python.org",
            "https://www.postgresql.org"
        ]

        ip_exemplo = ["192.168.1.10", "10.0.0.5", "172.16.0.25", "201.88.42.1"]

        for url_original in urls:
            codigo = "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=6))

            url_obj = UrlModel(
                urlOriginal=url_original,
                codigoGerado=codigo,
            )

            session.add(url_obj)
            session.commit()
            session.refresh(url_obj)

            num_clicks = random.randint(5,15)
            for _ in range(num_clicks):
                dias = random.randint(0,7)
                horas = random.randint(0, 23)
                data_click = datetime.now(timezone.utc) - timedelta(days=dias, hours=horas)

                click = ClickModel(
                    dataHora=data_click,
                    ip=fake.ipv4(),
                    url_id=url_obj.id,
                )

                session.add(click)

        session.commit()
        print("Bando de Dados populado com sucesso!")

if __name__ == "__main__":
    popular_banco()