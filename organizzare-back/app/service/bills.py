from dao import get_connection
from dao.bills import Bills_DAO
from datetime import datetime


class Bills_Service:
    def __init__(self):
        conn = get_connection()
        self.bills_DAO = Bills_DAO(conn)

    def create_bills(self, bill_type, value, code, residents_id):
        register_timestamp = datetime.now().isoformat()
        due_timestamp = datetime.now().isoformat()
        obj = self.bills_DAO.create_bills(bill_type, register_timestamp, due_timestamp, value, code, residents_id)
        return obj
    
    def update_bills(self, id, bill_type, register_timestamp, due_timestamp, value, code, residents_id):
        obj = self.bills_DAO.update_bills(id, bill_type, register_timestamp, due_timestamp, value, code, residents_id)
        return obj
    
    def get_bills(self, id):
        return_obj = self.bills_DAO.get_bills(id)
        return return_obj
    
    def list_bills(self):
        result = self.bills_DAO.list_bils()
        return result
        
    def get_bills_from_residents(self, residents_id):
        return self.bills_DAO.list_bills_from_residents(residents_id)