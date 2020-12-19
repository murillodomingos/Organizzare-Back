from flask import request
from controllers import app
from service.residents import Residents_Service
from service.bills import Bills_Service

bills_service = Bills_Service()
residents_service = Residents_Service()

@app.route('/residents', methods=['POST','GET'])
def create_residents_controller():
    if request.method == 'POST':
        data = request.get_json()   

        name = data['name']
        cpf = data['cpf']
        residents_pass = data['residents_pass']
        apartment_id = data['apartment_id']

        return residents_service.create_residents(name, cpf, residents_pass, apartment_id)
    
    if request.method == 'GET':
        resident = residents_service.list_residents()
        return resident
    return {
        'message': 'unknown operation'
    }

@app.route('/residents/<residents_id>', methods=['GET','PUT'])
def update_residents_controller(residents_id):
    if request.method == 'PUT':
        data = request.get_json()
        
        name = data['name']
        cpf = data['cpf']
        apartment_id = data['apartment_id']

        return residents_service.update_residents(residents_id, name, cpf, apartment_id)
    
    if request.method == 'GET':
        return residents_service.get_residents(residents_id)
    return {
        'message': 'unknown operation'
    }

@app.route('/residents/<residents_id>/bills', methods=['GET'])
def get_bills_from_residents(residents_id):
    return bills_service.get_bills_from_residents(residents_id)

@app.route('/residents/signin', methods=['POST'])
def signin_residents():
    if request.method == 'POST':
        data = request.get_json()

        cpf = data['cpf']
        resident_pass = data['resident_pass']

        return residents_service.residents_signin(cpf, resident_pass)
    return {
        'message': 'unknown operation'
    }
