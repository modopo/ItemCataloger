from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import session as login_session
from app.loginVerification import login_require

from app.db_setup import db_session, Categories, Items

category_owner = Blueprint('category_owner', __name__)


@category_owner.route('/category/<int:category_id>')
def showCategories(category_id):
    return "list of Categories"

@category_owner.route('/category/new',
           methods=['GET', 'POST'])
@login_require
def newCategory():
    return "This is a place to create a new category"

@category_owner.route('/category/<int:category_id>/edit',
           methods=['GET', 'POST'])
@login_require
def editCategory():
    return "This is where you edit a category"

@category_owner.route('/category/<int:category_id>/delete',
           methods=['GET', 'POST'])
@login_require
def deleteCategory():
    return "this is where you delete a category"
