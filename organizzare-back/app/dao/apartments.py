from traceback import print_exc

class Apartments_DAO:
    def __init__(self, conn):
        self.conn = conn
    
    def get_create_apartments_sql(self, number, block, condominium):
        sql = """
        insert into organizzare_app.apartments(id, number, block, condominium)
        values(uuid_generate_v4(), '{}','{}','{}')
        returning id, number, block, condominium
        """.format(number, block, condominium)
        return sql

    def create_apartments(self, number, block, condominium):

        trans = self.conn.begin()
        sql = self.get_create_apartments_sql(number, block, condominium)
        try:
            result = self.conn.execute(sql)
            trans.commit()
            for row in result:
                return {
                    'id': '{}'.format(row[0]),
                    "number": row[1],
                    'block': row[2],
                    'condominium': '{}'.format(row[3])
                }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when create apartment"
            }

    def get_upd_apartments_sql(self, id, changenumber, changeblock, changecondominium):
        sql_upd = """
        update organizzare_app.apartments    
        set number = '{}', block = '{}', condominium = '{}'
        where id = '{}'
        returning id, number, block, condominium
        """.format(changenumber, changeblock, changecondominium, id)
        return(sql_upd)

    def update_apartments(self, id, changenumber, changeblock, changecondominium):

        trans = self.conn.begin()
        sql_upd = self.get_upd_apartments_sql(id, changenumber, changeblock, changecondominium)
        
        try:
            result = self.conn.execute(sql_upd)
            trans.commit()
            for row in result:
                return {
                    'id': '{}'.format(row[0]),
                    "number":row[1],
                    'block':row[2],
                    'condominium':row[3]
                }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when update apartment"
            }

    def get_apartment_select_sql(self, id):
        sql = """
        select 
            id, "number", block, condominium
        from 
            organizzare_app.apartments a
        where   
            a.id='{}'
        """.format(id)
        return sql
    
    def get_apartments(self, id):
        trans = self.conn.begin()
        sql_get = self.get_apartment_select_sql(id)
        try:
            result = self.conn.execute(sql_get)
            trans.commit()
            for row in result:
                return {
                    'id': '{}'.format(row[0]),
                    "number": row[1],
                    'block': row[2],
                    'condominium': row[3],
                }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when get apartment"
            }

    def get_apartments_list_sql(self):
        sql = """
        select
            id, "number", block, condominium
        from 
            organizzare_app.apartments a
        """
        return sql
    
    def list_apartments(self):
        trans = self.conn.begin()
        sql_list = self.get_apartments_list_sql()
        try:
            result = self.conn.execute(sql_list)
            trans.commit()
            apartment=[]
            for row in result:
                apartments={
                    'id': '{}'.format(row[0]),
                    "number": row[1],
                    'block': row[2],
                    'condominium': row[3]
                }
                apartment.append(apartments)
            return {
                'apartment': apartment
            }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when list apartments"
            }

    def get_apartments_from_condominium_sql(self, condominium_id):
        sql = """
        select 
            id, "number", block, condominium from organizzare_app.apartments a 
        where 
            a.condominium='{}'
        """.format(condominium_id)
        return sql

    def list_apartments_from_condominium(self, condominium_id):
        trans = self.conn.begin()
        sql_list = self.get_apartments_from_condominium_sql(condominium_id)
        try:
            result = self.conn.execute(sql_list)
            trans.commit()
            apartment=[]
            for row in result:
                apartments={
                    'id': '{}'.format(row[0]),
                    "number": row[1],
                    'block': row[2],
                    'condominium': row[3]
                }
                apartment.append(apartments)
            return {
                'apartment': apartment
            }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when list apartments"
            }
