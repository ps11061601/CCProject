# from flask_wtf import FlaskForm
from wtforms import StringField, validators, Form, SelectField


class InputForm(Form):
    neighbourhood_group = SelectField(
        'Neighbourhood Group ', choices=[('', 'Select'), ('0', 'Bronx'), ('1', 'Brooklyn'), ('2', 'Manhattan'), 
                                           ('3', 'Queens'), ('4', 'Staten Island')],
        validators=[validators.InputRequired()])
    neighbourhood = SelectField(
        'Neighbourhood', choices=[('','Select'), ('0','Allerton'), ('1','Arden Heights'), ('2','Arrochar'), ('3','Arverne'), ('4','Astoria'),
       ('5','Bath Beach'), ('6','Battery Park City'), ('7','Bay Ridge'), ('8','Bay Terrace'),('9','Bay Terrace'), ("10",'Staten Island'),("11",'Baychester')], 
        validators=[validators.InputRequired()])
    room_type = SelectField(
        'Room Type ',choices=[('','Select'),('0','Entire home/apt'), ('1','Private room'), ('2','Shared room')],
        validators=[validators.InputRequired()])
    number_of_reviews = StringField(
        label='Number of Reviews ',
        validators=[validators.InputRequired()])
    reviews_per_month = StringField(
        label='Reviews per Month ',
        validators=[validators.InputRequired()])
    availability_365 = StringField(
        label='Availability ',
        validators=[validators.InputRequired()])
