from diagrams import Diagram, Cluster, Edge
from diagrams.programming.framework import Fastapi
from diagrams.onprem.database import Postgresql
from diagrams.onprem.container import Docker
from diagrams.onprem.client import Client

with Diagram("FastAPI Social Media App", show=False):
    
    with Cluster("Aplicação FastAPI"):
        docker_app = Docker("FastAPI Docker")
        app = Fastapi("FastAPI")
        docker_app - app

    with Cluster("Banco de dados"):
        docker_db = Docker("PostgreSQL Docker")
        db = Postgresql("PostgreSQL")
        db - docker_db

    swagger = Client("Swagger UI")

    swagger >> Edge(color="green") >> app
    app >> Edge(color="green") >> swagger
    app >> Edge(color="brown", style="dashed") >> db
    db >> Edge(color="brown", style="dashed") >> app
