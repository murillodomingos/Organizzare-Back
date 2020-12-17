from dao import get_connection
from dao.residents import Residents_DAO
from datetime import datetime

class Residents_Service():
    def __init__(self):
        conn = get_connection()
        self.residents_DAO = Residents_DAO(conn)

    def create_residents(self, name, cpf, apartment_id):
        register_timestamp = datetime.now().isoformat()
        obj = self.residents_DAO.create_residents(name, cpf, register_timestamp, apartment_id)
        return obj

    def update_residents(self, id, name, cpf, apartment_id):
        obj = self.residents_DAO.update_residents(id, name, cpf, apartment_id)
        return obj
    
    def get_residents(self, id):
        return_obj = self.residents_DAO.get_residents(id)
        return return_obj
    
    def list_residents(self):
        result = self.residents_DAO.list_residents()
        return result

    def get_residents_from_apartments(self, condominium_id):
        return self.residents_DAO.list_residents_from_apartments(condominium_id)