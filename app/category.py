from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import session as login_session

from app.db_setup import db_session, Categories, Items

@app.route('/')
@app.route('/category')
def showCategories():
    return "list of Categories"

@app.route('/category/new',
           methods=['GET', 'POST'])
def newCategory():
    return "This is a place to create a new category"

@app.route('/category/<int:category_id>/edit',
           methods=['GET', 'POST'])
def editCategory():
    return "This is where you edit a category"

@app.route('/category/<int:category_id>/delete',
           methods=['GET', 'POST'])
def deleteCategory():
    return "this is where you delete a category"
