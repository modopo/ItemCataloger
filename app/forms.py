import instance.config as config
from flask import session
from wtforms import Form, StringField, validators
from wtforms.csrf.session import SessionCSRF

class BaseForm(Form):
    class Meta:
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = config.APP_SECRET_KEY

        @property
        def csrf_context(self):
            return session

# validates category form is made
class categoryForm(BaseForm):
    name = StringField('name', [validators.Length(min=1, max=250)])

# validates item form is made
class itemForm(BaseForm):
    name = StringField('name', [validators.Length(min=1, max=250)])
    description = StringField('description', [validators.Length(min=1,
                                                                max=1000)])
