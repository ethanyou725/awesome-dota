from flask import  Flask
from flask_bootstrap import Bootstrap



app = Flask(__name__)
app.config['SECRET_KEY'] = 'today is 20161126'
# testapp.config?????
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return '<h1>404</h1>'




if __name__ =="__main__":
    app.run(debug=True)