from wtforms import Form, IntegerField, StringField


class mockingForm(Form):
    textToMockify = StringField('Your text here')


class rolldiceForm(Form):
    dicenumber = IntegerField('Number of dice')
    dicesides = IntegerField('Sides of dice')
