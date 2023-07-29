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

### Como Acessar a Documentação da API (FastAPI Docs) para Realizar Operações CRUD

A aplicação FastAPI Social Media App possui uma documentação abrangente da API que permite interagir com a API e realizar operações CRUD (Criar, Ler, Atualizar, Excluir) nos posts de forma fácil. Para acessar a documentação da API, siga os passos abaixo:

1. **Executar a Aplicação FastAPI**: Certifique-se de seguir as etapas de configuração mencionadas no arquivo `README.md` para executar o FastAPI Social Media App usando o Docker Compose. Verifique se a aplicação está em execução ao executar o comando `docker-compose up`.
    
2. **Abrir a Documentação da API**: Com o aplicativo FastAPI em execução, abra o navegador da web e acesse o seguinte URL:
    
    ```bash
    http://localhost:8000/docs
    ```
    
    O URL acima irá levá-lo para o FastAPI Docs, uma documentação interativa integrada fornecida pelo FastAPI.
    
3. **Explorar os Endpoints da API**: Ao acessar o FastAPI Docs, você verá uma interface amigável que exibe todos os endpoints da API disponíveis. O FastAPI Social Media App oferece os seguintes endpoints para os posts:
    
    * **GET `/`**: Endpoint raiz com uma mensagem "Hello World".
    * **GET `/posts`**: Obter todos os posts.
    * **GET `/posts/{id}`**: Obter um post específico por ID.
    * **POST `/posts`**: Criar um novo post.
    * **DELETE `/posts/{id}`**: Excluir um post por ID.
    * **PUT `/posts/{id}`**: Atualizar um post por ID.
4. **Interagir com os Endpoints**: Você pode interagir com cada endpoint clicando nele. A interface exibirá os parâmetros necessários (se houver) e os modelos de resposta. Você também pode testar as diferentes operações CRUD inserindo os dados necessários e clicando em "Try it out!".
    
5. **Testar Operações CRUD**: Use o FastAPI Docs para realizar várias operações CRUD nos posts. Por exemplo:
    
    * Para criar um novo post, clique no endpoint `POST /posts`, insira o `title`, `content` e `published`, em seguida, clique em "Execute".
    * Para recuperar todos os posts, clique no endpoint `GET /posts` e clique em "Execute".
    * Para atualizar um post, clique no endpoint `PUT /posts/{id}`, insira o `id`, `title`, `content` e `published` do post que deseja atualizar, em seguida, clique em "Execute".
    * Para excluir um post, clique no endpoint `DELETE /posts/{id}`, insira o `id` do post que deseja excluir e clique em "Execute".
6. **Resposta da API**: Após realizar uma operação, o FastAPI Docs exibirá a resposta recebida da API, permitindo que você verifique os resultados.
    

A documentação da API fornecida pelo FastAPI torna fácil entender e testar as funcionalidades da API sem a necessidade de ferramentas adicionais ou software externo. Divirta-se testando e explorando o FastAPI Social Media App!