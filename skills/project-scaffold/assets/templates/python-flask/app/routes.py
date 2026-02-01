"""
USER IMPLEMENTATION REQUIRED

Define your application routes here.

Tasks for this stage:
{{STAGE_TASKS}}
"""

from flask import Blueprint, jsonify

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return jsonify({"message": "Hello World!"})

# TODO: Add your routes here
# Example:
# @bp.route('/api/endpoint')
# def your_endpoint():
#     # IMPLEMENT: Your logic here
#     pass
