from flask_bootstrap import Bootstrap
import sys
from flask import Flask, render_template, flash, redirect, url_for, session


# sys.path.append("..")
# import scripts.DataHandler
# import scripts.HeroList
from scripts import DataHandler
from scripts import HeroList


app = Flask(__name__)
app.config['SECRET_KEY'] = 'today is 20161126'
# testapp.config?????
bootstrap = Bootstrap(app)

@app.route('/error')
def index():
    return '<h1>404 Not Found</h1>'

@app.route('/')
def home():
    list=HeroList.Names
    return render_template('show.html',post=list)


@app.route('/hero/1')
def detail():
    pass


if __name__ =="__main__":
    app.run(debug=True)
