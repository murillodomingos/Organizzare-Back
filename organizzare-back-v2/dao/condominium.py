from connection import get_connection

class Condominium_DAO:
    def __init__(self, conn):
        self.conn = conn
        
    def get_create_condominium_sql(self, name, cep, address, number, city):
        sql = """
        insert into organizzare_app.condominium(id, name, cep, address, number, city)
        values(uuid_generate_v4(),'{}','{}','{}','{}','{}')
        """.format(name, cep, address, number, city)
        return sql

    def create_condominium(self, name, cep, address, number, city):

        trans = self.conn.begin()
        sql = self.get_create_condominium_sql(name, cep, address, number, city)
        self.conn.execute(sql)
        trans.commit()

conn = get_connection()
DAO = Condominium_DAO(conn)

DAO.create_condominium('rua mais bonita', '14171115', 'jardim das flores', '223', 'tiradentes')

