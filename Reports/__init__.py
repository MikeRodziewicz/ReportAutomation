from flask import Flask


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'


from Reports.Core.views import core

app.register_blueprint(core)