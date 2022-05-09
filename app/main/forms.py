from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,SelectField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User
from wtforms import ValidationError






class pitchForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired])
    pitch = TextAreaField('write your pitch here',validators=[DataRequired])
    category = SelectField('Choose your prefered category',choices=[('health','health'), ('comedy','comedy'), ('business','business')],validators=[DataRequired])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('write your comment here    ', validators=[DataRequired()])
    submit = SubmitField('Pitch')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):

 title = StringField('Pitch title',validators=[DataRequired()])

 pitch = TextAreaField('User pitch')

 submit = SubmitField('Submit')



class CommentForm(FlaskForm):

 title = StringField('Pitch title',validators=[DataRequired()])

 comment = TextAreaField('User comment')

 submit = SubmitField('Submit') 
    