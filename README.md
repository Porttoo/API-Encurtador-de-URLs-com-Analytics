
# API Encurtador de URLs com Analytics

API RESTful desenvolvida em Python com FastAPI para encurtartamento de URLs, redirecionamento e recolha de métricas de acesso (analytics). O projeto utiliza uma arquitetura modular, persistência relacional com PostgreSQL e suporte completo a conteinerização via Docker.


## O Problema e Solução

- **O Problema:** Ferramentas tradicionais de encurtamento de URLs existem em grande quantidade, mas limitam-se em redirecionar o utilizador sem oferecer qualquer tipo de retorno sobre o desempenho, alcance ou origem de acesso, o que dificulta a análise de campanhas ou compartilhamentos.

- **A Solução:** Uma aplicação robusta que não apenas encurta URLs longas, mas que também processa o redirecionamento (utilizando o código HTTP adequado) enquanto registra de forma estruturada os metadados de cada clique (como o endereço ip e o carimbo de data/hora) em um banco de dados relacional PostgreSQL. Adicionalmente, disponibiliza um endpoint analítico dedicado para a consulta do histórico de acessos por link.
## Stack Tecnológica

- **Lnguagem:** Python 3.11+
- **Framework Web:** FastAPI
- **ORM:** SQLModel/SQLAlchemy
- **Banco de Dados:** PostgreSQL
- **Gerenciamento:** Docker & Docker Compose
- **Gestão de Dados Falsos:** Faker


## Estrutura de Projeto e Descrição do Componentes

O código está organizado de forma modular para garantir a separação de responsabilidades:

- `main.py`: Ponto de entrada da aplicação, configuração do FastAPI e definição das rotas principais.
- `model.py`: Definição de modelos de dados relacionais (UrlModel e ClickModel) utilizando SQLModel.
- `schemas.py`: Schemas Pydantic para validação e serialização dos dados de entrada e saída.
- `database.py` : configuraçãoda sessão e da conexão com o banco de dados PostgreSQL.
- `services.py` : Camada de serviço contendo lógica de negócio (encurtamento, registro de cliques e cálculo de analytics).
- `seeder.py` : Script para povoar o banco de dados com registros simulados realistas para fins de demonstração.
- `Dockerfile` : Instruções para a criação da imagem Docker da aplicação.
- `docker-compose.yml` : Gerenciamento de serviços da API e do banco de dados PostgreSQL. 


## Endpoints da API

1. `POST /url`
        
    Cria e devolve um código encurtado para uma URL original fornecida
    
2. `GET /{codigo}`

    Redireciona o utilizador para a URL original associada ao código e registra automaticamente o clique (incluindo timestamp e endereço IP).
    
3. `GET /analytics/{codigo}`

    Retorna as métricas detalhadas de um link, incluindo o número total de cliques e o histórico de acessos recentes.
## Como Executar o Projeto com Docker

### Pré-requisito
- Docker e Docker Compose instalados

### 1. Clonar o repositório

```bash
git clone https://github.com/Porttoo/API-Encurtador-de-URLs-com-Analytics.git
cd "API Encurtador de URLs com Analytics"
```

### 2. Configurar o arquivo de Variaveis de Ambiente (.env)

Crie um arquivo `.env` na raiz do projeto para devinir a senha do banco de dados de forma segura:

```Snippet de código
DB_PASSWORD=sua_senha_aqui
```
### 3. Subir os Containers

Execute o seguinte comando no terminal para iniciar o banco de dados e a aplicação:

```bash
docker-compose up --build
```

### 5. Povoar o Banco de dados

Com os containers em execução, abra um novo terminal e execute o script de seed para inserir URLs e dados de cliques simulados:

```bash
docker exec -it encurtador_api python seeder.py
```

### 6.Acessando Documentação Interativa (Swagger UI)

Acesse através do navegador para testar os endpoints

- **Swagger UI:** http://localhost:8000/docs
## Autor

Gabriel Porto | Porttoo

- [GitHub](https://github.com/Porttoo)
- [Linkedin](https://www.linkedin.com/in/gabrielrosaporto/)

