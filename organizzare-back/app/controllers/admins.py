from flask import request
from controllers import app
from service.admins import Admins_Service

admins_service = Admins_Service()

@app.route('/admins', methods=['POST','GET'])
def create_admins_controller():
    if request.method == 'POST':
        data = request.get_json()   

        name = data['name']
        phone = data['phone']
        cpf = data['cpf']
        user_type = data['user_type']
        user_pass = data['user_pass']

        return admins_service.create_admins(name, phone, cpf, user_type, user_pass)
    
    if request.method == 'GET':
        admin = admins_service.list_admins()
        return admin
    return {
        'message': 'unknown operation'
    }

@app.route('/admins/<admins_id>', methods=['GET','PUT'])
def update_admins_controller(admins_id):
    if request.method == 'PUT':
        data = request.get_json()
        
        name = data['name']
        phone = data['phone']
        cpf = data['cpf']
        user_type = data['user_type']

        return admins_service.update_admins(admins_id, name, phone, cpf, user_type)
    
    if request.method == 'GET':
        return admins_service.get_admins(admins_id)
    return {
        'message': 'unknown operation'
    }

@app.route('/admins/<admins_id>/condominium/<condominium_id>', methods=['POST'])
def create_admins_condomoniums(admins_id, condominium_id):
    if request.method == 'POST':
        data = request.get_json()
        
        admins_id = data['admins_id']
        condominium_id = data['condominium_id']

        return admins_service.create_admins_condomoniums(admins_id, condominium_id)
    return {
        'message': 'unknown operation'
    }

@app.route('/admins/<admin_cpf>/condominium', methods=['GET'])
def get_admin_condominium(admin_cpf):
    if request.method == 'GET':
        data = request.get_json()

        admin_cpf = data['admin_cpf']
        return admins_service.get_admin_condominium(admin_cpf)
    return {
        'message': 'unknown operation'
    }

@app.route('/admins/signin', methods=['POST'])
def signin_admin():
    if request.method == 'POST':
        data = request.get_json()

        cpf = data['cpf']
        user_pass = data['user_pass']

        return admins_service.admin_signin(cpf, user_pass)
    return {
        'message': 'unknown operation'
    }
