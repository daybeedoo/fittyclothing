from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email

class LoginForm(FlaskForm):
	username = StringField('Username', validators = [InputRequired()])
	password = PasswordField('Password' validators = [InputRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators = [InputRequired()])
	email = StringField('Email', validators = [InputRequired(), Email(message = 'Invalid Email Address')])
	password = PasswordField('Password' validators = [InputRequired()])
	confirm_password = PasswordField('Confirm Password' validators = [InputRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Register')

	