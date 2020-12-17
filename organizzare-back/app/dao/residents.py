from traceback import print_exc


class Residents_DAO:
    def __init__(self, conn):
        self.conn = conn

    def get_create_residents_sql(self, name, cpf, register_timestamp, apartment_id):
        sql = """
        insert into organizzare_app.residents(id, name, cpf, register_timestamp, unregister_timestamp, apartment_id)
        values(uuid_generate_v4(),'{}','{}','{}', NULL,'{}')
        returning id, name, cpf, register_timestamp, apartment_id
        """.format(name, cpf, register_timestamp, apartment_id)
        return sql

    def create_residents(self, name, cpf, register_timestamp, apartment_id):

        trans = self.conn.begin()
        sql = self.get_create_residents_sql(name, cpf, register_timestamp, apartment_id)
        try:
            result = self.conn.execute(sql)
            trans.commit()
            for row in result:
                return {
                    'id':'{}'.format(row[0]),
                    'name':row[1],
                    'cpf':row[2],
                    'register_timestamp':row[3],
                    'apartment_id':row[4]
                }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when create residents"
            }

    def get_upd_resident_sql(self, id, changename, changecpf, changeapartment_id):

        sql_upd = """
        update organizzare_app.residents
        set name = '{}', cpf = '{}', apartment_id = '{}'
        where id = '{}'
        returning id, name, cpf, register_timestamp, apartment_id
        """.format(changename, changecpf, changeapartment_id, id)
        return(sql_upd)

    def update_residents(self, id, changename, changecpf, changeapartment):

        trans = self.conn.begin()
        sql_upd = self.get_upd_resident_sql(id, changename, changecpf, changeapartment)
        try:
            result = self.conn.execute(sql_upd)
            trans.commit()
            for row in result:
                return {
                    'id':'{}'.format(row[0]),
                    'name':row[1],
                    'cpf':row[2],
                    'register_timestamp':row[3],
                    'apartment_id':row[4]
                }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when update residents"
            }
    
    def get_residents_select_sql(self, id):
        sql = """
        select 
            id, name, cpf, register_timestamp, apartment_id
        from 
            organizzare_app.residents r
        where   
            r.id='{}'
        """.format(id)
        return sql
    
    def get_residents(self, id):
        trans = self.conn.begin()
        sql_get = self.get_residents_select_sql(id)
        try:
            result = self.conn.execute(sql_get)
            trans.commit()
            for row in result:
                return {
                    'id':'{}'.format(row[0]),
                    'name':row[1],
                    'cpf':row[2],
                    'register_timestamp':row[3],
                    'apartment_id':row[4]
                }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when get residents"
            }

    def get_residents_list_sql(self):
        sql = """
        select
            id, name, cpf, register_timestamp, apartment_id
        from 
            organizzare_app.residents r
        """
        return sql
    
    def list_residents(self):
        trans = self.conn.begin()
        sql_list = self.get_residents_list_sql()
        try:
            result = self.conn.execute(sql_list)
            trans.commit()
            resident=[]
            for row in result:
                residents={
                    'id':'{}'.format(row[0]),
                    'name':row[1],
                    'cpf':row[2],
                    'register_timestamp':row[3],
                    'apartment_id':row[4]
                }
                resident.append(residents)
            return {
                'resident': resident
            }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when list residents"
            }
    
    def get_residents_from_apartments_sql(self, apartment_id):
        sql = """
        select 
            id, name, cpf, register_timestamp, apartment_id
        from
            organizzare_app.residents r
        where
            r.apartment_id='{}'
        """.format(apartment_id)
        return sql

    def list_residents_from_apartments(self, apartment_id):
        trans = self.conn.begin()
        sql_list = self.get_residents_from_apartments_sql(apartment_id)
        try:
            result = self.conn.execute(sql_list)
            trans.commit()
            resident=[]
            for row in result:
                residents={
                    'id':'{}'.format(row[0]),
                    'name':row[1],
                    'cpf':row[2],
                    'register_timestamp':row[3],
                    'apartment_id':row[4]
                }
                resident.append(residents)
            return {
                'resident': resident
            }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when list residents"
            }    

