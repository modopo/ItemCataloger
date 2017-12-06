from app.db_setup import db_session, User

def create_user(login_session):
    newUser = User(name = login_session['username'], email = login_session[
        'email'], picture = login_session['picture'])
