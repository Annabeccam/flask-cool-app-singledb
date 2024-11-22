# encoding: utf-8

from flask import Flask
from best_app.config import DbConfig
from flask_migrate import Migrate
from flask_restful import Resource, Api
from best_app.database import db
from flask_cors import CORS
from best_app.modules.user import UserList 
from best_app.modules.car import CarList 

def create_app():    
    app = Flask(__name__)    
      
    app.config.from_mapping(
        SECRET_KEY = "My_Secret_Key"
    )
    
    app.config.from_object(DbConfig)
    #app.cofig[]   
    CORS(app, origins=['http://localhost:3000'])  

    db.init_app(app)
    from best_app.models.user import User
    from best_app.models.car import Car

    migrate = Migrate(app, db)

    #app.register_blueprint(hello.blueprint)
    #app.register_blueprint(goodbye.blueprint)
    #app.register_blueprint(user.blueprint)
    #app.register_blueprint(as.blueprint)
    #app.register_blueprint(user.blueprint)


    api=Api(app) 
    api.add_resource(UserList, '/users')
    api.add_resource(CarList, '/cars')

    #api.add_resource(AsiaUserList, '/asiausers')
    #api.add_resource(EuropeCarList, '/europecars')


    return app