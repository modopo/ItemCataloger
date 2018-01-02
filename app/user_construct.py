from app.db_setup import db_session, User

"""Helper methods that create user and gets user info"""


def user_create(login_session):
    new_user = User(name=login_session['username'], email=login_session[
        'email'], picture=login_session['picture'])
    db_session.add(new_user)
    db_session.commit()
    user = db_session.query(User).filter_by(email=login_session[
        'email']).one()
    return user.id


def user_get(user_id):
    user = db_session.query(User).filter_by(id=user_id).one()
    return user


def user_get_id(user_email):
    try:
        user = db_session.query(User).filter_by(email=user_email).one()
        return user.id
    except:
        return None
