from flask import request, jsonify
from controllers import app
from service.bills import Bills_Service

bills_service = Bills_Service()

@app.route('/bills', methods=['POST', 'GET'])
def create_bills_controllers():
    if request.method == 'POST':
        data = request.get_json()

        bill_type = data['bill_type']
        value = data['value']
        code = data['code']
        resident = data['resident']

        return bills_service.create_bills(bill_type, value, code, resident)
        
    if request.method == 'GET':
        return bills_service.list_bills()
    return {
        'message': 'unknown operation'
    }

@app.route('/bills/<bills_id>', methods=['GET','PUT'])
def update_bills_controller(bills_id):
    if request.method == 'PUT':
        data = request.get_json()
        
        bill_type = data['bill_type']
        register_timestamp = data['register_timestamp']
        due_timestamp = data['due_timestamp']
        value = data['value']
        code = data['code']
        resident = data['resident']

        return bills_service.update_bills(bills_id, bill_type, register_timestamp, due_timestamp, value, code, resident)
    
    if request.method == 'GET':
        return bills_service.get_bills(bills_id)
    return {
        'message': 'unknown operation'
    }

