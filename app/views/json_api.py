from flask import Blueprint, jsonify
from app.db_setup import db_session, Categories, Items

api_blueprint = Blueprint('api', __name__)


# JSON API endpoint just for categories
@api_blueprint.route('/category/JSON')
def all_categories_json():
    categories = db_session.query(Categories).all()
    return jsonify(categories=[x.serialize for x in categories])


# JSON API endpoint for items in a certain category
@api_blueprint.route('/category/<int:category_id>/JSON')
def all_item_in_category_json(category_id):
    items = db_session.query(Items).filter_by(id=category_id).all()
    return jsonify(items=[x.serialize for x in items])


# JSON API endpoint for a specific item
@api_blueprint.route('/category/<int:category_id>/item/<int:item_id>/JSON')
def item_json(item_id, category_id):
    details = db_session.query(Items).filter_by(id=item_id).one()
    return jsonify(item=details.serialize)
