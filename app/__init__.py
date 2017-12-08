from flask import Flask

from .views.index import index
from .views.category import category_owner
from .views.items import item_owner
from .views.jsonAPI import api
from .views.oauth_connect import user_owner


app = Flask(__name__)
app.register_blueprint(index)
app.register_blueprint(category_owner)
app.register_blueprint(item_owner)
app.register_blueprint(api)
app.register_blueprint(user_owner)