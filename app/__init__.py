from flask import Flask

from .views.index import index_blueprint
from .views.category import category_blueprint
from .views.items import item_blueprint
from .views.jsonAPI import api_blueprint
from .views.oauth_connect import oauth_blueprint

app = Flask(__name__)
app.register_blueprint(index_blueprint)
app.register_blueprint(category_blueprint)
app.register_blueprint(item_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(oauth_blueprint)
