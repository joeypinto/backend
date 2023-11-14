from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import (
    jsonify,
    request,
    Blueprint
)
from serverbase.extensions import csrf
from serverbase.blueprints.test_request.models.tr_code_table import TestRequestCode
from serverbase.blueprints.test_request.models.new_test_request import NewTestRequest
from serverbase.blueprints.test_request.schemas.new_test_request_schemas import new_test_request_graph_schema, new_test_request_schema
from flask_login import current_user
graph = Blueprint('graph', __name__)

csrf.exempt(graph)
@graph.route("/graph/", methods=["GET"])
def get():
    initialDate = request.args.get('initialDate', None)  
    finalDate = request.args.get('finalDate', None)  
    selected_type = request.args.get('selected_type', None)  
    location = request.args.get('location', None)  
    metho_type = request.args.get('metho_type', None)
    return jsonify(TestRequestCode.find_graph(initialDate,finalDate,selected_type, metho_type, location))
    
    
csrf.exempt(graph)
@graph.route("/allTestRequest/", methods=["GET"])
def allTestRequest():
    selected_type = request.args.get('selected_type', None)  
    return jsonify(new_test_request_schema.dump(NewTestRequest.allTestRequest(selected_type), many=True))    
    