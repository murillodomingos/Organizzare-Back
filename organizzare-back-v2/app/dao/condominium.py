class Condominium_DAO:
    def __init__(self, conn):
        self.conn = conn
        
    def get_create_condominium_sql(self, name, cep, address, number, city):
        sql = """
        insert into organizzare_app.condominium(id, name, cep, address, number, city)
        values(uuid_generate_v4(),'{}','{}','{}','{}','{}')
        returning id
        """.format(name, cep, address, number, city)
        return sql

    def create_condominium(self, name, cep, address, number, city):

        trans = self.conn.begin()
        sql = self.get_create_condominium_sql(name, cep, address, number, city)
        result = self.conn.execute(sql)
        trans.commit()
        for row in result:
            return row[0]
