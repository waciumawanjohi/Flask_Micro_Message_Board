from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import validators

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired(), validators.Length(min=8,max=32)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
