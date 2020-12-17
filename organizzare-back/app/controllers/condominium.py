from flask import request
from controllers import app
from service.condominium import Condominium_Service
from service.apartments import Apartments_Service


condominium_service = Condominium_Service()
apartments_service = Apartments_Service()

@app.route('/condominium', methods=['POST','GET'])
def create_condominium_controller():
    if request.method == 'POST':
        data = request.get_json()
        
        name = data['name']
        cep = data['cep']
        address = data['address']
        number = data['number']
        city = data['city']

        return condominium_service.create_condominium(name, cep, address, number, city)
    
    if request.method == 'GET':
        condominiums = condominium_service.list_condominium()
        return condominiums
    return {
        'message': 'unknown operation'
    }

@app.route('/condominium/<condominium_id>', methods=['GET','PUT'])
def update_condominium_controller(condominium_id):
    if request.method == 'PUT':
        data = request.get_json()
        
        name = data['name']
        cep = data['cep']
        address = data['address']
        number = data['number']
        city = data['city']

        return condominium_service.update_condominium(condominium_id, name, cep, address, number, city)
    
    if request.method == 'GET':
        return condominium_service.get_condominium(condominium_id)
    return {
        'message': 'unknown operation'
    }

@app.route('/condominium/<condominium_id>/apartments', methods=['GET'])
def get_apartments_from_condominium(condominium_id):
    return apartments_service.get_apartments_from_condominium(condominium_id)
    

