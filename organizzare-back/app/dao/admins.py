from traceback import print_exc

class Admins_DAO:
    def __init__(self, conn):
        self.conn = conn
    
    def get_create_admins_sql(self, name, phone, cpf, register_timestamp, user_type, user_hash):
        sql = """
        insert into organizzare_app.admins(id, name, phone, cpf, register_timestamp, unregister_timestamp, user_type, user_hash)
        values(uuid_generate_v4(), '{}','{}','{}','{}', NULL, '{}', '{}')
        returning id, name, phone, cpf, register_timestamp, user_type
        """.format(name, phone, cpf, register_timestamp, user_type, user_hash)
        return sql

    def create_admins(self, name, phone, cpf, register_timestamp, user_type, user_hash):

        trans = self.conn.begin()
        sql = self.get_create_admins_sql(name, phone, cpf, register_timestamp, user_type, user_hash)
        try:
            result = self.conn.execute(sql)
            trans.commit()
            for row in result:
                return {
                    'id': '{}'.format(row[0]),
                    'name': row[1],
                    'phone': row[2],
                    'cpf': row[3],
                    'register_timestamp': row[4],
                    'user_type': row[5]            
                }
        except:
            print_exc()
            trans.rollback()
            raise Exception( "error happened when create admin")

    def get_upd_admins_sql(self, id, changename, changephone, changecpf, changeuser_type):
        sql_upd = """
        update organizzare_app.admins  
        set name = '{}', phone = '{}', cpf = '{}', user_type = '{}'
        where id = '{}'
        returning id, name, phone, cpf, register_timestamp, user_type
        """.format(changename, changephone, changecpf, changeuser_type, id)
        return(sql_upd)

    def update_admins(self, id, changename, changephone, changecpf, changeuser_type):
        trans = self.conn.begin()
        sql_upd = self.get_upd_admins_sql(id, changename, changephone, changecpf, changeuser_type)
        
        try:
            result = self.conn.execute(sql_upd)
            trans.commit()
            for row in result:
                return {
                    'id': '{}'.format(row[0]),
                    'name': row[1],
                    'phone': row[2],
                    'cpf': row[3],
                    'register_timestamp': row[4],
                    'user_type': row[5],
                }
        except:
            print_exc()
            trans.rollback()
            raise Exception( "error happened when update admin")

    def get_admins_select_sql(self, id):
        sql = """
        select 
            id, name, phone, cpf, register_timestamp, user_type
        from 
            organizzare_app.admins d
        where   
            d.id='{}'
        """.format(id)
        return sql
    
    def get_admins(self, id):
        trans = self.conn.begin()
        sql_get = self.get_admins_select_sql(id)
        try:
            result = self.conn.execute(sql_get)
            trans.commit()
            for row in result:
                return {
                    'id': '{}'.format(row[0]),
                    'name': row[1],
                    'phone': row[2],
                    'cpf': row[3],
                    'register_timestamp': row[4],
                    'user_type': row[5],
                }
        except:
            print_exc()
            trans.rollback()
            raise Exception( "error happened when get admin")

    def get_admins_list_sql(self):
        sql = """
        select
            id, name, phone, cpf, register_timestamp, user_type
        from 
            organizzare_app.admins n
        """
        return sql
    
    def list_admins(self):
        trans = self.conn.begin()
        sql_list = self.get_admins_list_sql()
        try:
            result = self.conn.execute(sql_list)
            trans.commit()
            admin=[]
            for row in result:
                admins={
                    'id': '{}'.format(row[0]),
                    'name': row[1],
                    'phone': row[2],
                    'cpf': row[3],
                    'register_timestamp': row[4],
                    'user_type': row[5],
                }
                admin.append(admins)
            return {
                'all': admin
            }
        except:
            print_exc()
            trans.rollback()
            raise Exception( "error happened when list admin")
    
    def create_admins_condomoniums_sql(self, admins_id, condominium_id):
        sql = """
        insert into organizzare_app.admins_condominiums(condominium_id, admins_id)
        VALUES('{}', '{}')
        returning condominium_id, admins_id
        """.format(condominium_id, admins_id)
        return sql

    def create_admins_condomoniums(self, condominium_id, admins_id):

        trans = self.conn.begin()
        sql = self.create_admins_condomoniums_sql(condominium_id, admins_id)
        try:
            result = self.conn.execute(sql)
            trans.commit()
            for row in result:
                return {
                    'admins_id': '{}'.format(row[0]),
                    'condominium': '{}'.format(row[1])
                }
        except:
            print_exc()
            trans.rollback()
            raise Exception( "error happened when create ralationship admin/condominium")

    def get_condominiums_from_admin_sql(self, cpf):
        sql = """
            select 
                a.name, c.id, c.name as condominium_name, cep, address, "number", city
            from 
                organizzare_app.admins a 
            left join 
                organizzare_app.admins_condominiums ac on a.id = ac.admins_id
            inner join 
                organizzare_app.condominium c on c.id = ac.condominium_id
            where 
                a.cpf = '{}'   
            """.format(cpf)
        return sql

    def get_admin_condominium(self, cpf):

        trans = self.conn.begin()
        sql = self.get_condominiums_from_admin_sql(cpf)
        try:
            result = self.conn.execute(sql)
            trans.commit()
            condominiums=[]
            for row in result:
                condominium={
                    'name': row[0],
                    'condominium_id': '{}'.format(row[1]),
                    'condominium_name': row[2],
                    'cep': row[3],
                    'address': row[4],
                    "number": row[5],
                    'city': row[6]
                }
                condominiums.append(condominium)
            return {
                'condominiums': condominiums
            }
        except:
            print_exc()
            trans.rollback()
            raise Exception( "error happened when create ralationship admin/condominium")

    def get_hash_from_admin_sql(self, cpf):
        sql  = """
        select 
            user_hash, id, user_type
        from 
            organizzare_app.admins a 
        where 
            a.cpf = '{}'
        """.format(cpf)
        return sql

    def get_hash_from_admin(self, cpf):
        trans = self.conn.begin()
        try:
            sql_get = self.get_hash_from_admin_sql(cpf)
            result = self.conn.execute(sql_get)
            trans.commit()
            for row in result:
                return {
                    'hash': '{}'.format(row[0]),
                    'id': '{}'.format(row[1]),
                    'user_type': 'admin'
                }
            raise Exception ('cpf nao existe')
        except:
            print_exc()
            trans.rollback()
            raise Exception("error happened when get admin")
