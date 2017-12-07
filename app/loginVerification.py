from functools import wraps
from flask import redirect
from flask import session as login_session

def login_require(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if 'username' not in login_session:
            return redirect('/login')
        else:
            return function(*args, **kwargs)
    return wrapper