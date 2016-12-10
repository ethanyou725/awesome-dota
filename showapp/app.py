from flask_bootstrap import Bootstrap
import sys
from flask import Flask, render_template, flash, redirect, url_for, jsonify,request
import os
import json
from flask.ext.cache import Cache
from flask_debugtoolbar import DebugToolbarExtension

sys.path.append("..")
# import scripts.DataHandler
# import scripts.HeroList
from scripts.DataHandler import RESULT,DATE_RANGE,DataFileList
from scripts import HeroList
from scripts.DownloadImages import url_list


app = Flask(__name__)
app.config['SECRET_KEY'] = 'today is 20161126'
# app.debug=True

# testapp.config?????
bootstrap = Bootstrap(app)
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

@app.route('/error')
def index():
    return '<h1>404 Not Found</h1>'

@app.route('/')
@cache.cached(timeout=300)
def home():
    a = []
    for n in range(112):
        a.append([HeroList.Names[n], url_list[n]])

    return render_template('show.html',post=a)


@app.route('/hero/<index>')
@cache.cached(timeout=300)
def detail(index):
    num=int(index)-1
    result1=[]
    result2=[]
    for i in range(DataFileList.__len__()):
        result1.append(RESULT[i]['rate'][num])
        result2.append(RESULT[i]['frequency'][num])

    # print(HeroList.Names[num])
    data={
        'name':HeroList.Names[num],
        'rate':result1,
        'frequency':result2,
        'date':DATE_RANGE
    }

    return json.dumps(data,ensure_ascii=False,indent=2)





if __name__ =="__main__":
    app.config.update(
        TEMPLATES_AUTO_RELOAD=True,
        DEBUG=True,
        DEBUG_TB_PROFILER_ENABLED=True,
        DEBUG_TB_TEMPLATE_EDITOR_ENABLED=True
    )

    extra_dir = os.path.dirname(os.path.abspath("."))
    extra_files=[]


    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = os.path.join(dirname, filename)
            if os.path.isfile(filename):
                extra_files.append(filename)

    toolbar = DebugToolbarExtension(app)

    app.run(extra_files=extra_files)

