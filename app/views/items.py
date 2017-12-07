from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import session as login_session
from app.loginVerification import login_require

from app.db_setup import db_session, Categories, Items

item_owner = Blueprint('item_owner', __name__)


@item_owner.route('/category/<int:category_id>/item/<int:item_id>')
def showItem(category_id, item_id):
    category = db_session.query(Categories).filter_by(id = category_id).one()
    items = db_session.query(Items).filter_by(category_id = category_id).all()
    return "this is where you list out items for that particular category"

@item_owner.route('/category/<int:category_id>/new',
           methods=['GET', 'POST'])
@login_require
def createItem(category_id):
    return "this is where you create a new item for that particular category"

@item_owner.route('/category/<int:category_id>/item/<int:item_id>/edit',
           methods=['GET', 'POST'])
@login_require
def editItem(category_id, item_id):
    return "this is where you edit an item"

@item_owner.route('/category/<int:category_id>/item/<int:item_id>/delete',
           methods=['GET', 'POST'])
@login_require
def deleteItem(category_id, item_id):
    return "this is where you delete an item"
