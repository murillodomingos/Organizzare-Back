from dao import get_connection
from dao.apartments import Apartments_DAO


class Apartments_Service():
    def __init__(self):
        conn = get_connection()
        self.apartments_DAO = Apartments_DAO(conn)

    def create_apartments(self, number, block, condominium):
        obj = self.apartments_DAO.create_apartments(number, block, condominium)
        return obj

    def update_apartments(self, id, number, block, condominium):
        obj = self.apartments_DAO.update_apartments(id, number, block, condominium)
        return obj

    def get_apartments(self, id):
        result_obj = self.apartments_DAO.get_apartments(id)
        return result_obj
    
    def list_apartments(self):
        result = self.apartments_DAO.list_apartments()
        return result

    def get_apartments_from_condominium(self, condominium_id):
        return self.apartments_DAO.list_apartments_from_condominium(condominium_id)
