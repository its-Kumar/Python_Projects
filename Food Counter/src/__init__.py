import connexion
from flask_cors import CORS
from src.config.enviroment import HOST, PORT


def init_api():
    app = connexion.App(__name__, specification_dir="./swagger/")
    app.add_api('swagger.yaml', arguments={"host_with_port": f"{HOST}:{PORT}"})
    CORS(app.app)
    return app
