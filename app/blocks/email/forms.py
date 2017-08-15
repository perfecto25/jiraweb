from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.fields.html5 import DateField

# Set your classes here.
 

class RegisterForm(FlaskForm):
    name = StringField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = StringField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(),
        EqualTo('password', message='Passwords must match')]
    )

class form_email_init(FlaskForm):
    jira_key = StringField(label='Jira #', 
                           render_kw={"style":"width:150px"},
                           validators=[DataRequired(), Length(min=3, max=10)])

    submit = SubmitField("Lookup Jira", render_kw={"class": "btn btn-primary btn-block", "style":"align:right"})


class form_email_prod_change(FlaskForm):
    #jira_key = StringField(label='Jira #', validators=[DataRequired(), Length(min=3, max=10)])
    notes = StringField('Notice', validators=[DataRequired(), Length(min=1, max=55)])
    date = DateField('Date of Change', render_kw={"style":"width:200px"}, validators=[DataRequired()])
    submit = SubmitField("Send", render_kw={"class": "btn btn-primary btn-block", "style":"align:right"})


    # password = PasswordField(
    #     'Password', validators=[DataRequired(), Length(min=6, max=40)]
    # )
    # confirm = PasswordField(
    #     'Repeat Password',
    #     [DataRequired(),
    #     EqualTo('password', message='Passwords must match')]
    # )

# class LoginForm(Form):
#     name = TextField('Username', [DataRequired()])
#     password = PasswordField('Password', [DataRequired()])


# class ForgotForm(Form):
#     email = TextField(
#         'Email', validators=[DataRequired(), Length(min=6, max=40)]
#     )