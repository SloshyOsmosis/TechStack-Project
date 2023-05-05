from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class SignupForm(FlaskForm):
    firstname = StringField("First Name",validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired()])
    phonenum = StringField("Phone Number", validators=[DataRequired(),Length(min=1, max=11)])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in")