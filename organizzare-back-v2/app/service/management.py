from dao import get_connection
from dao.condominium import Condominium_DAO


def management_start():
    
    conn = get_connection()
    DAO = Condominium_DAO(conn)

    condominiumID = DAO.create_condominium('rua mais bonita22', '14171115', 'jardim das flores', '223', 'tiradentes')
    print(condominiumID)