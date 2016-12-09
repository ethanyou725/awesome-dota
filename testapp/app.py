import random
from flask import Flask, render_template, flash, redirect, url_for, session

from flask_bootstrap import Bootstrap
from testapp.app_forms import GuessNumberForm
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'today is 20161124'
app.debug=True
# testapp.config?????
bootstrap = Bootstrap(app)
toolbar = DebugToolbarExtension(app)

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
            flash('Congratulation!!!', 'success')
            return redirect(url_for('.index'))
    return render_template('guess.html', form=form)


if __name__ == '__main__':
    app.run()
