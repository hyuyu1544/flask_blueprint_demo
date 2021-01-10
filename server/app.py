from flask import Flask
from .blueprint1 import Blueprint1
from .blueprint2 import Blueprint2


app = Flask(__name__)


app.register_blueprint(Blueprint1, url_prefix="/blueprint1")
app.register_blueprint(Blueprint2, url_prefix="/blueprint2")
