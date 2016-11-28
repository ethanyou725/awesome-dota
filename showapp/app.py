from flask_bootstrap import Bootstrap
import sys
from flask import Flask, render_template, flash, redirect, url_for, jsonify,request
import os

# sys.path.append("..")
# import scripts.DataHandler
# import scripts.HeroList
from scripts.DataHandler import RESULT,DATE_RANGE
from scripts import HeroList
from scripts.DownloadImages import EName,url_list


app = Flask(__name__)
app.config['SECRET_KEY'] = 'today is 20161126'
# testapp.config?????
bootstrap = Bootstrap(app)

@app.route('/error')
def index():
    return '<h1>404 Not Found</h1>'

@app.route('/')
def home():
    a = []
    for n in range(112):
        a.append([HeroList.Names[n], url_list[n]])

    return render_template('show.html',post=a)


@app.route('/hero/<index>')
def detail(index):
    num=int(index)-1
    print(type(num))

    data={
        'rate':RESULT['rate'][num],
        'frequency':RESULT['frequency'][num],
    }
    return jsonify(data)





if __name__ =="__main__":
    app.config.update(
        DEBUG=True,
        TEMPLATES_AUTO_RELOAD=True,
    )
    extra_dir = os.path.dirname(os.path.abspath("."))
    extra_files=[]


    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = os.path.join(dirname, filename)
            if os.path.isfile(filename):
                extra_files.append(filename)
    app.run(extra_files=extra_files)

