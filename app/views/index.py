from flask import Blueprint, render_template
from sqlalchemy import asc, desc
from app.db_setup import db_session, Categories, Items

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/')
@index_blueprint.route('/category')
def index():
    categories = db_session.query(Categories).order_by(asc(Categories.name))
    items = db_session.query(Items).order_by(desc(Items)).limit(5)
    return render_template('index.html', categories= categories, items = items)