from flask import Flask
from src.main.routes.tag_router import tags_routes_bp

app = Flask(__name__)

app.register_blueprint(tags_routes_bp)
