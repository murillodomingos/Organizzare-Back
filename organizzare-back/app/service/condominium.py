from dao import get_connection
from dao.condominium import Condominium_DAO


class Condominium_Service:
    def __init__(self):
        conn = get_connection()
        self.condominium_DAO = Condominium_DAO(conn)

    def create_condominium(self, name, cep, address, number, city):
        obj = self.condominium_DAO.create_condominium(name, cep, address, number, city)
        return obj

    def update_condominium(self, id, name, cep, address, number, city):
        obj = self.condominium_DAO.update_condominium(id, name, cep, address, number, city)
        return obj

    def get_condominium(self, id):
        result_obj = self.condominium_DAO.get_condominium(id)
        return result_obj
    
    def list_condominium(self):
        result = self.condominium_DAO.list_condominium()
        return result
