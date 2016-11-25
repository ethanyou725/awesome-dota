import random
from flask import Flask, render_template, flash, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very hard to guess string'

bootstrap = Bootstrap(app)


@app.route('/')
def index():
    session['number'] = random.randint(0, 1000)
    session['count'] = 10
    return render_template('index.html')


@app.route('/guess', methods=['POST',"GET"])
def guess():
    times = session['count']
    result = session.get('number')
    form = GuessNumberForm()
    if form.validate_on_submit():
        times -= 1
        session['count'] = times
        if times == 0:
            flash('sorry you lose!', 'danger')
            return redirect(url_for('.index'))
        answer = form.number.data

        if answer > result:
            flash('too big! %s times' % times, 'warning')
        elif answer < result:
            flash('too small %s times！' % times, 'info')
        else:
            flash('Congratulation', 'success')
            return redirect(url_for('.index'))
    return render_template('guess.html', form=form)


class GuessNumberForm(FlaskForm):
    number = IntegerField('输入一个整数(0~1000)', validators=[
        DataRequired('请输入一个有效的整数！'),
        NumberRange(0, 1000, '请输入0~1000以内的整数！')])
    submit = SubmitField('提交')


if __name__ == '__main__':
    app.run(debug=True)
