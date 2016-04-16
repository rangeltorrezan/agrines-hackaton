# -*- coding: utf-8 -*-nexxera_flask_response

import json

from flasgger.utils import swag_from
from flask import abort
from flask import request, Blueprint

from controller.rest import get_datastore_session


# bp = Blueprint('manejo', __name__)
# parse_path = ParsePath(20)
#
# @swag_from('swagger/manejo/get.yml')
# @bp.route("/manejo", methods=['GET'])
# def list_all_payment():
#     args = parse_path.parse(request.args)
#     repository = PaymentRepository()
#     response = repository.find(get_datastore_session(), args)
#     return json.dumps(response, cls=JSONEncoder)
#
#
# @swag_from('swagger/manejo/get-by-id.yml')
# @bp.route("/manejo/<id>", methods=['GET'])
# def search_payment_by_id(id):
#     repository = PaymentRepository()
#     payment = repository.get(get_datastore_session(), id)
#     if not payment:
#         abort(404)
#
#     return json.dumps(payment, cls=JSONEncoder)
#
# @swag_from('swagger/manejo/put.yml')
# @bp.route("/manejo/<id>", methods=['PUT'])
# def update_payment(id):
#     if not request.json:
#         abort(400)
#
#     repository = PaymentRepository()
#     datastore = get_datastore_session()
#     payment = repository.first(datastore, **{'uuid': id})
#
#     if not payment:
#         abort(404)
#
#     payment_updated = repository.update(datastore, payment, **request.json)
#     return json.dumps(payment_updated, cls=JSONEncoder)
#
#
# @swag_from('swagger/manejo/put.yml')
# @bp.route("/manejo/<id>/detail", methods=['GET'])
# def payment_detail_by_id(id):
#
#     repository = PaymentHistoryRepository()
#     datastore = get_datastore_session()
#     payment_detail = repository.find(datastore, **{'uuid_payment': id})
#
#     return json.dumps(payment_detail, cls=JSONEncoder)
