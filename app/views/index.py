from flask import Blueprint, render_template
from sqlalchemy import asc, desc
from app.db_setup import db_session, Categories, Items

index = Blueprint('index', __name__)

@index.route('/')
@index.route('/catalogue')
def index():
    categories = db_session.query(Categories).order_by(asc(Categories.name))
    items = db_session.query(Items).order_by(desc(Items))