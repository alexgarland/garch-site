from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class StockForm(Form):
    stock = StringField('Stock Symbol', validators=[DataRequired()])