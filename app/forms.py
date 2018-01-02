import config
from flask import session
from wtforms import Form, StringField, validators
from wtforms.csrf.session import SessionCSRF


class BaseForm(Form):
    """ Classes that enable helper method to validate input in forms"""

    class Meta:
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = config.CSRF_SECRET_KEY

        @property
        def csrf_context(self):
            return session


# validates category form is made
class CategoryForm(BaseForm):
    name = StringField('name', [validators.Length(min=1, max=250)])


# validates item form is made
class ItemForm(BaseForm):
    name = StringField('name', [validators.Length(min=1, max=250)])
    description = StringField('description', [validators.Length(min=1,
                                                                max=1000)])
