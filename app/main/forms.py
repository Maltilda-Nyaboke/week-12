from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,SelectField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User
from wtforms import ValidationError






class pitchForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired])
    pitch = StringField('Pitch',validators=[DataRequired])
    category = SelectField('Category',choices=[('health','health'), ('comedy','comedy'), ('business','business')],validators=[DataRequired])
    submit = SubmitField('Pitch')



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')