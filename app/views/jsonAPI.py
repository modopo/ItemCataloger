from flask import Blueprint, jsonify

from app.db_setup import db_session, Categories, Items
api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/category/JSON')
def allCategoriesJSON():
    categories = db_session.query(Categories).all()
    return jsonify(categories = [x.serialize for x in categories])

@api_blueprint.route('/category/<int:category_id>/JSON')
def allItemInCategoryJSON(category_id):
    items = db_session.query(Items).filter_by(id = category_id).all()
    return jsonify(items = [x.serialize for x in items])

@api_blueprint.route('/category/<int:category_id>/item/<int:item_id>')
def itemJSON(item_id):
    details = db_session.query(Items).filter_by(id = item_id).one()
    return jsonify(item = details.serialize)