from flask import request
from controllers import app
from service.apartments import Apartments_Service
from service.residents import Residents_Service

apartments_service = Apartments_Service()
residents_service = Residents_Service()

@app.route('/apartments', methods=['POST', 'GET'])
def create_apartments_controller():
    if request.method == 'POST':
        data = request.get_json()

        number = data['number']
        block = data['block']
        condominium = data['condominium']

        return apartments_service.create_apartments(number, block, condominium)

    if request.method == 'GET':
        apartments = apartments_service.list_apartments()
        return apartments
    return {
        'message': 'unknown operation'
    }

@app.route('/apartments/<apartments_id>', methods=['GET', 'PUT'])
def update_apartments_controller(apartments_id):
    if request.method == 'PUT':
        data = request.get_json()

        number = data['number']
        block = data['block']
        condominium = data['condominium']

        return apartments_service.update_apartments(apartments_id, number, block, condominium)
    
    if request.method == 'GET':
        return apartments_service.get_apartments(apartments_id)

    return {
        'message': 'unknown operation'
    }

@app.route('/apartments/<apartments_id>/residents', methods=['GET'])
def get_residents_from_apartments(apartments_id):
    return residents_service.get_residents_from_apartments(apartments_id)

