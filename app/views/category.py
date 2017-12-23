from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import session as login_session

from app.forms import categoryForm
from app.decoratorlogin import login_require

from app.db_setup import db_session, Categories, Items

category_blueprint = Blueprint('category_owner', __name__)

# displays all the items within the category
@category_blueprint.route('/category/<int:category_id>')
def showCategories(category_id):
    category = db_session.query(Categories).filter_by(id = category_id).one()
    items = db_session.query(Items).filter_by(category_id = category_id).all()
    return render_template('category.html', category_id = category_id,
                           category = category, items = items)
# create a new category
@category_blueprint.route('/category/new',
                          methods=['GET', 'POST'])
@login_require
def newCategory():
    form = categoryForm(request.form)
    if request.method == 'POST' and form.validate():
        new = Categories(name = request.form['name'],
                         user_id = login_session['user_id'])
        db_session.add(new)
        db_session.commit()
        flash('Category {} has been successfully created!'.format(new.name))
        return redirect(url_for('home.index'))
    return render_template('/newcategory.html', form = form)

@category_blueprint.route('/category/<int:category_id>/edit',
                          methods=['GET', 'POST'])
@login_require
def editCategory(category_id):
    edit = db_session.query(Categories).filter_by(id = category_id).one()
    form = categoryForm(request.form)

    if edit.user_id != login_session['user_id']:
        flash('Unauthorized to edit this category')
        return redirect(url_for('category_owner.showCategory',
                                category_id = category_id))
    if request.method == 'POST' and form.validate():
        edit.name = request.form['name']
        db_session.add(edit)
        db_session.commit()
        flash('Category {} has been successfully edited!'.format(edit.name))
        return redirect(url_for('category_owner.showCategories', category_id = category_id))
    else:
        return render_template('/editcategory.html', category = edit,
                               form = form)

@category_blueprint.route('/category/<int:category_id>/delete',
                          methods=['GET', 'POST'])
@login_require
def deleteCategory(category_id):
    delete = db_session.query(Categories).filter_by(id = category_id).one()
    form = categoryForm(request.form)
    if delete.user_id != login_session['user_id']:
        flash('Unauthorized to delete this category')
        return redirect(url_for('category_owner.showCategory',
                                category_id = category_id))
    if request.method == 'POST':
        db_session.delete(delete)
        db_session.commit()
        flash('Category {} successfully deleted!'.format(delete.name))
        return redirect(url_for('home.index'))
    else:
        return render_template('/deletecategory.html', category = delete,
                               form = form)
