from traceback import print_exc

class Condominium_DAO:
    def __init__(self, conn):
        self.conn = conn
        
    def get_create_condominium_sql(self, name, cep, address, number, city):
        sql = """
        insert into organizzare_app.condominium(id, name, cep, address, number, city)
        values(uuid_generate_v4(),'{}','{}','{}','{}','{}')
        returning id, name, cep, address, number, city
        """.format(name, cep, address, number, city)
        return sql

    def create_condominium(self, name, cep, address, number, city):

        trans = self.conn.begin()
        sql = self.get_create_condominium_sql(name, cep, address, number, city)
        try:
            result = self.conn.execute(sql)
            trans.commit()
            for row in result:
                return {
                    'id': '{}'.format(row[0]),
                    'name': row[1],
                    'cep': row[2],
                    'address': row[3],
                    "number": row[4],
                    'city': row[5]
                }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when create condominium"
            }

    def get_upd_condominium_sql(self, id, changename, changecep, changeaddress, changenumber, changecity):
        sql_upd = """
        update organizzare_app.condominium
        set name = '{}', cep = '{}', address = '{}', number = '{}', city = '{}'
        where id = '{}'
        returning id, name, cep, address, number, city
        """.format(changename, changecep, changeaddress, changenumber, changecity, id)
        return(sql_upd)

    def update_condominium(self, id, changename, changecep, changeaddress, changenumber, changecity):

        trans = self.conn.begin()
        sql_upd = self.get_upd_condominium_sql(id, changename, changecep, changeaddress, changenumber, changecity)
        try:
            result = self.conn.execute(sql_upd)
            trans.commit()
            for row in result:
                return {
                    'id': '{}'.format(row[0]),
                    'name': row[1],
                    'cep': row[2],
                    'address': row[3],
                    "number": row[4],
                    'city': row[5]
                }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when update condominum"
            }

    def get_condominium_select_sql(self, id):
        sql = """
        select 
            id, name, cep, address, "number", city 
        from 
            organizzare_app.condominium c 
        where   
            c.id='{}'
        """.format(id)
        return sql
    
    def get_condominium(self, id):
        trans = self.conn.begin()
        sql_get = self.get_condominium_select_sql(id)
        try:
            result = self.conn.execute(sql_get)
            trans.commit()
            for row in result:
                return {
                    'id': '{}'.format(row[0]),
                    'name': row[1],
                    'cep': row[2],
                    'address': row[3],
                    "number": row[4],
                    'city': row[5]
                }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when get condominium"
            }

    def get_condominium_list_sql(self):
        sql = """
        select
            id, name, cep, address, "number", city 
        from 
            organizzare_app.condominium c 
        """
        return sql
    
    def list_condominium(self):
        trans = self.conn.begin()
        sql_list = self.get_condominium_list_sql()
        try:
            result = self.conn.execute(sql_list)
            trans.commit()
            condominiums=[]
            for row in result:
                condominium={
                    'id': '{}'.format(row[0]),
                    'name': row[1],
                    'cep': row[2],
                    'address': row[3],
                    "number": row[4],
                    'city': row[5]
                }
                condominiums.append(condominium)
            return {
                'condominiums': condominiums
            }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when list condominium"
            }
    