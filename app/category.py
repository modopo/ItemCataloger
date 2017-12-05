from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import session as login_session

app = Flask(__name__)

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

@app.route('/category/<int:category_id>')
@app.route('/category/<int:category_id>/items')
def showItems(category_id):
    return "this is where you list out items for that particular category"

@app.route('/category/<int:category_id>/new',
           methods=['GET', 'POST'])
def createItem(category_id):
    return "this is where you create a new item for that particular category"

@app.route('/category/<int:category_id>/<int:item_id>/edit',
           methods=['GET', 'POST'])
def editItem(category_id, item_id):
    return "this is where you edit an item"

@app.route('/category/<int:category_id>/<int:item_id>/delete',
           methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    return "this is where you delete an item"
