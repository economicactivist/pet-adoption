from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, TextAreaField
from wtforms.fields.core import BooleanField
from wtforms.validators import Optional


class AddPetForm(FlaskForm):
    name = StringField("Pet name: ")
    species = StringField("Species name: ")
    photo_url = StringField("Photo URL (optional): ", validators=[Optional()])
    age = IntegerField("Age (optional): ", validators=[Optional()])
    notes = TextAreaField("Notes (optional): ", validators=[Optional()])
    available = BooleanField("Available", validators=[Optional()])



# Create a form for adding pets. This should use Flask-WTF, and should have the following fields:

# Pet name
# Species
# Photo URL
# Age
# Notes
# This should be at the URL path /add. Add a link to this from the homepage.