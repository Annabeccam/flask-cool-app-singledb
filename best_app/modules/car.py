# encoding: utf-8

from flask import Blueprint
from flask import g, current_app
from best_app.database import db
from best_app.models.car import Car 
import flask_restful as restful
from flask import jsonify
import json

#blueprint = Blueprint('db1', __name__, url_prefix='/db1')
blueprint = Blueprint('db1',__name__)

class CarList(restful.Resource):
    #get_parser = reqparse.RequestParser()
    #get_parser.add_argument('include_archived', type=str, default=None, location='args')
    #get_parser.add_argument('since_ts', type=int, default=0, location='args')

    #@auth.login_required
    #@requires_admin
    #@marshal_with(alert_fields)
    def get(self):
        #args = self.get_parser.parse_args()
        #return "hello"
        q = Car.query.all()
        print(q[0].username)
        #u = jsonify(q)
        #users = q.all()
        import jsonpickle
        j = jsonpickle.encode(q)
        #q.dump(q)
        #u = json.dumps(q, default=vars)
        return j

'''
@blueprint.route("/db1", methods=["GET"])
def say_bye():
    return "Goodbye!"
'''