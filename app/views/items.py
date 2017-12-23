from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import session as login_session

from sqlalchemy import asc

from app.forms import itemForm
from app.decoratorlogin import login_require

from app.db_setup import db_session, Categories, Items

item_blueprint = Blueprint('item_owner', __name__)

# displays item properties
@item_blueprint.route('/category/<int:category_id>/item/<int:item_id>')
def showItem(category_id, item_id):
    item = db_session.query(Items).filter_by(id = item_id).one()
    category = db_session.query(Categories).filter_by(id = category_id).one()
    return render_template('item.html', category_id = category_id,
                                        item_id = item_id,
                                        category = category,
                                        item = item)

# create a new item
@item_blueprint.route('/category/<int:category_id>/new',
                      methods=['GET', 'POST'])
@login_require
def newItem(category_id):
    form = itemForm(request.form)
    if request.method == 'POST' and form.validate():
        new = Items(name = request.form['name'],
                    description = request.form['description'],
                    category_id = category_id,
                    user_id = login_session['user_id'])
        db_session.add(new)
        db_session.commit()
        flash('New item {} successfully created!'.format(new.name))
        return redirect(url_for('category_owner.showCategories', category_id = category_id))
    return render_template('newitem.html', category_id = category_id, form = form)

@item_blueprint.route('/category/<int:category_id>/item/<int:item_id>/edit',
                      methods=['GET', 'POST'])
@login_require
def editItem(category_id, item_id):
    edit = db_session.query(Items).filter_by(id = item_id).one()
    category = db_session.query(Categories).filter_by(id=category_id).one()
    form = itemForm(request.form)

    if edit.user_id != login_session['user_id']:
        flash('Unauthorized to edit this item')
        return redirect(url_for('category_owner.showCategory',
                                category_id = category_id))
    if request.method == 'POST' and form.validate():
        if request.form['name']:
            edit.name = request.form['name']
        if request.form['description']:
            edit.description = request.form['description']
        db_session.add(edit)
        db_session.commit()
        flash('Item {} edited successfully!'.format(edit.name))
        return redirect(url_for('item_owner.showItem', category_id = category_id, item_id = item_id))
    else:
        return render_template('/edititem.html', category = category,
                                                item = edit, form = form)

@item_blueprint.route('/category/<int:category_id>/item/<int:item_id>/delete',
                      methods=['GET', 'POST'])
@login_require
def deleteItem(category_id, item_id):
    delete = db_session.query(Items).filter_by(id = item_id).one()
    form = itemForm(request.form)
    if delete.user_id != login_session['user_id']:
        flash('Unauthorized to delete this item')
        return redirect(url_for('category_owner.showCategory',
                                category_id = category_id))
    if request.method == 'POST':
        db_session.delete(delete)
        db_session.commit()
        flash('Item {} successfully deleted!'.format(delete.name))
        return redirect(url_for('category_owner.showCategories', category_id = category_id))
    else:
        return render_template('/deleteitem.html', category_id = category_id,
                               item_id = item_id, item = delete, form = form)

