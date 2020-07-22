from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import CalculatorForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    form = CalculatorForm()
    if form.validate_on_submit():
        payment = round(form.principal.data * (form.interest_rate.data / 100 / 12) * (form.interest_rate.data / 100 / 12 + 1) ** (form.loan_term.data*12) / ((1 + form.interest_rate.data / 100 / 12) ** (form.loan_term.data * 12) -1), 2)
        noi = round((form.rent.data - form.hoa.data) * 12, 2)
        cap_ratio = round((form.rent.data - form.hoa.data) * 12 / form.price.data * 100, 2)
        rent_cost_ratio = round(form.rent.data / form.price.data * 100, 2)
        gross_yield_ratio = round(form.rent.data * 12 / form.price.data * 100, 2)
        debt_service_ratio = round(noi / 12 / payment, 4)

        flash('Results:')
        flash('Monthly Mortgage Payment={}'.format(payment))
        flash('Net Operating Income(NOI)={}'.format(noi))
        flash('Capitalization Ratio={}%'.format(cap_ratio))
        flash('Rent Cost Ratio={}%'.format(rent_cost_ratio))
        flash('Gross Yield Ratio={}%'.format(gross_yield_ratio))
        flash('Debt Service Ratio={}'.format(debt_service_ratio))

        return redirect(url_for('calculator'))
    return render_template('calculator.html', title='Calculator', form=form)
