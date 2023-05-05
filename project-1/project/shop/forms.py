from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TextAreaField, IntegerField, DecimalField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, NumberRange

class ItemForm(FlaskForm):
    id = HiddenField()
    name = StringField("Name", validators=[DataRequired(), Length(max=30)])
    description = TextAreaField("Description", validators=[DataRequired()])
    category = StringField("Category", validators=[DataRequired(), Length(max=30)])
    stock = IntegerField("Stock", validators=[Optional(), NumberRange(min=0)])
    unit_price = DecimalField("Unit Price", validators=[Optional(), NumberRange(min=0)])
    visibility = BooleanField("Visibility")
    submit = SubmitField("Save")

class CheckoutForm(FlaskForm):
    payment_methods = [("Cash", "Cash"), ("Visa", "Visa"), ("MasterCard", "MasterCard"), ("Amex", "Amex")]
    payment_method = SelectField("Payment Method", choices=payment_methods)
    total_amount = DecimalField("Total Amount", validators=[DataRequired()])
    first_name = StringField("First Name", validators=[DataRequired(), Length(max=30)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(max=10)])
    apartment = StringField("Apartment, Suite, etc.", validators=[DataRequired(), Length(max=30)])
    city = StringField("City", validators=[DataRequired(), Length(max=15)])
    state = StringField("State", validators=[DataRequired(), Length(max=15)])
    country = StringField("Country", validators=[DataRequired(), Length(max=15)])
    postal_code = StringField("Postal Code", validators=[DataRequired(), Length(max=15)])
    submit = SubmitField("Checkout")
