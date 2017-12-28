from app.db_setup import db_session, User


def userCreate(login_session):
    newUser = User(name=login_session['username'], email=login_session[
        'email'], picture=login_session['picture'])
    db_session.add(newUser)
    db_session.commit()
    user = db_session.query(User).filter_by(email=login_session[
        'email']).one()
    return user.id


def userGet(user_id):
    user = db_session.query(User).filter_by(id=user_id).one()
    return user


def userGetId(user_email):
    try:
        user = db_session.query(User).filter_by(email=user_email).one()
        return user.id
    except:
        return None
