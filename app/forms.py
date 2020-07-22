from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField
from wtforms.validators import DataRequired

class CalculatorForm(FlaskForm):
    price = DecimalField('Total Property Price', validators=[DataRequired()])
    principal = DecimalField('Mortgage Principal', validators=[DataRequired()])
    interest_rate = DecimalField('Interest Rate/ %', validators=[DataRequired()])
    loan_term = DecimalField('Loan Term/years', validators=[DataRequired()])
    rent = DecimalField('Estimated Rent/month', validators=[DataRequired()])
    hoa = DecimalField('HOA/Condo Fee', validators=[DataRequired()])
    submit = SubmitField('Calculate')
