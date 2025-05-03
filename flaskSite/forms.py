from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed

class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    intro = StringField('Intro', validators=[DataRequired(), Length(max=200)])
    text = TextAreaField('Content', validators=[DataRequired()])
    image = FileField('Image', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField('Create Article')