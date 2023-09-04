from flask import Flask
from flask_restx import Api


app = Flask(__name__)

api = Api(
    app,
    title="Proyecto ML_OPS",
    version="0.1",
    description="Endpoints"
)
