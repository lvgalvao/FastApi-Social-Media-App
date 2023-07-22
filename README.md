# FastAPI Social Media App

Uma aplicação simples de CRUD com Python <br/>
Módulo API da funcionalidade posts de uma rede social

## Tecnologias Usadas

* FastAPI
* Docker

## Configuração do Projeto

### Requisitos

* Python 3.11.3
* Docker
* Docker Compose

### Como Executar

1. Clone este repositório em sua máquina local.
2. Navegue até a pasta do projeto em um terminal.
3. Execute o comando `docker-compose up`.

O comando acima irá:

* Construir uma imagem Docker para o aplicativo usando o `Dockerfile` na pasta do projeto.
* Iniciar um contêiner Docker usando essa imagem.
* Mapear a porta 8000 dentro do contêiner Docker para a porta 8000 em sua máquina local.
* Montar a pasta do projeto dentro do contêiner Docker, de modo que as alterações feitas na pasta do projeto em sua máquina local sejam refletidas dentro do contêiner.

Uma vez que o contêiner esteja rodando, você pode acessar o aplicativo navegando para `http://localhost:8000` em seu navegador web.