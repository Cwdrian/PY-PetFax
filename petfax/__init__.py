from flask import Flask
from . import pets

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "this is my homepage"
    
    
    app.register_blueprint(pets.bp)

    @app.route('/pets')
    def pets(): 
        return 'These are our pets available for adoption!'

    return app