import requests
from flask import Flask, render_template

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    
    @app.route('/')
    def index():


        # subjects = [
        # {
        #     "nombre":"AC",
        #     "creditos":"6"
        # },
        # {
        #     "nombre":"SO",
        #     "creditos":"6"
        # }
        # ]


        url = "https://api.fib.upc.edu/v2/assignatures/"
        response = requests.get(url)
        datos = response.json()
        print(datos)       
        subjects = datos.results
        return render_template('base.html', subjects = subjects)

    # a simple page that says hello, used to test app factory
    #from . import dashboard
    # maps references the main application behavior
    # (couldn't be called app for obvious reasons)
    #app.register_blueprint(dashboard.bp)

    return app