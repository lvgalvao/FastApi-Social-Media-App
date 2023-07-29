# Aplicativo de Mídia Social com FastAPI

Olá pessoal, nesse projeto criamos um aplicativo simples de CRUD com Python, utilizando o módulo API para a funcionalidade de postagens em uma rede social.

## Tecnologias Usadas

* FastAPI
* Postgress
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

## Como Acessar a Documentação da API (FastAPI Docs) para Realizar Operações CRUD

Com o aplicativo FastAPI em execução, abra o navegador da web e acesse o seguinte URL:

```bash
http://localhost:8000/docs
```

A aplicação FastAPI Social Media App possui uma documentação abrangente da API que permite interagir com a API e realizar operações CRUD (Criar, Ler, Atualizar, Excluir) nos posts de forma fácil. Para acessar a documentação da API, siga os passos abaixo:
    
1. **Explorar os Endpoints da API**: Ao acessar o FastAPI Docs, você verá uma interface amigável que exibe todos os endpoints da API disponíveis. O FastAPI Social Media App oferece os seguintes endpoints para os posts:
    
    * **GET `/`**: Endpoint raiz com uma mensagem "Hello World".
    * **GET `/posts`**: Obter todos os posts.
    * **GET `/posts/{id}`**: Obter um post específico por ID.
    * **POST `/posts`**: Criar um novo post.
    * **DELETE `/posts/{id}`**: Excluir um post por ID.
    * **PUT `/posts/{id}`**: Atualizar um post por ID.
    


A documentação da API fornecida pelo FastAPI torna fácil entender e testar as funcionalidades da API sem a necessidade de ferramentas adicionais ou software externo. Divirta-se testando e explorando o FastAPI Social Media App!