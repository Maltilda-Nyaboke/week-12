from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User



class RegistrationForm(FlaskForm):
    email = StringField('Your email address',validators=[DataRequired(),Email()])
    username = StringField('Your username',validators=[DataRequired])