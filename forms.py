from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, TextAreaField


class AddPetForm(FlaskForm):
    name = StringField("Pet name: ")
    species = StringField("Species name: ")
    photo_url = StringField("Photo URL (optional): ")
    age = IntegerField("Age (optional): ")
    notes = TextAreaField("Notes (optional): ")



# Create a form for adding pets. This should use Flask-WTF, and should have the following fields:

# Pet name
# Species
# Photo URL
# Age
# Notes
# This should be at the URL path /add. Add a link to this from the homepage.