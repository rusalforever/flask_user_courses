from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length


class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=6, max=50)])
    email = StringField('E-mail', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    phone = StringField('Phone')
    mobile_phone = StringField('Mobile phone')
    status = SelectField('Status', coerce=int, choices=[(0, 'Inactive'), (1, 'Active')], )
    submit = SubmitField('Create')
