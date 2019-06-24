from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, equal_to

#To register a user
class RegistrationForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

        email = StringField('Email', validators=[DataRequired(), Email()])

        password = PasswordField('Password', validators=[DataRequired()])
        confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), equal_to('password')])

        submit = SubmitField('Sign Up')

#The user login

class LoginForm(FlaskForm):
       # username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

        email = StringField('Email', validators=[DataRequired(), Email()])

        password = PasswordField('Password', validators=[DataRequired()])
        #confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), equal_to('password')])

        remember = BooleanField('Remeber Me')
        submit = SubmitField('Sign Up')