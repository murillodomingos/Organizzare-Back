from traceback import print_exc

class Bills_DAO:
    def __init__(self, conn):
        self.conn = conn

    def get_create_bills_sql(self, bill_type, register_timestamp, due_timestamp, value, code, resident):
        sql = """
        insert into organizzare_app.bills(id, bill_type, register_timestamp, due_timestamp, value, code, resident)
        values(uuid_generate_v4(),'{}','{}','{}','{}','{}','{}')
        returning id, bill_type, register_timestamp, due_timestamp, value, code, resident
        """.format(bill_type, register_timestamp, due_timestamp, value, code, resident) 
        return sql
    
    def create_bills(self, bill_type, register_timestamp, due_timestamp, value, code, resident):

        trans = self.conn.begin()
        sql = self.get_create_bills_sql(bill_type, register_timestamp, due_timestamp, value, code, resident)
        try:
            result = self.conn.execute(sql)
            trans.commit()
            for row in result:
                return {
                    'id' : '{}'.format(row[0]),
                    'bill_type' : row[1],
                    'register_timestamp' : row[2],
                    'due_timestamp' : row[3],
                    'value' : '{}'.format(row[4]),
                    'code' : row[5],
                    'resident' : row[6]
                }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when create bills"
            }


    def get_upd_bills_sql(self, id, changebill_type, changeregister_timestamp, changedue_timestamp, changevalue, changecode, changeresident):
        sql_upd = """
        update organizzare_app.bills
        set bill_type = '{}', register_timestamp = '{}', due_timestamp = '{}', value = '{}', code = '{}', resident = '{}'
        where id = '{}'
        returning id, bill_type, register_timestamp, due_timestamp, value, code, resident
        """.format(changebill_type, changeregister_timestamp, changedue_timestamp, changevalue, changecode, changeresident, id)
        return(sql_upd)

    def update_bills(self, id, changebill_type, changeregister_timestamp, changedue_timestamp, changevalue, changecode, changeresident):

        trans = self.conn.begin()
        sql_upd = self.get_upd_bills_sql(id, changebill_type, changeregister_timestamp, changedue_timestamp, changevalue, changecode, changeresident)
        try:
            result = self.conn.execute(sql_upd)
            trans.commit()
            for row in result:
                return {
                    'id' : '{}'.format(row[0]),
                    'bill_type' : row[1],
                    'register_timestamp' : row[2],
                    'due_timestamp' : row[3],
                    'value' : '{}'.format(row[4]),
                    'code' : row[5],
                    'resident' : row[6]
                }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when update bills"
            }
        
    def get_bills_select_sql(self, id):
        sql = """
        select 
            id, bill_type, register_timestamp, due_timestamp, value, code, resident
        from 
            organizzare_app.bills b
        where   
            b.id='{}'
        """.format(id)
        return sql
    
    def get_bills(self, id):
        trans = self.conn.begin()
        sql_get = self.get_bills_select_sql(id)
        try:
            result = self.conn.execute(sql_get)
            trans.commit()
            for row in result:
                return {
                    'id' : '{}'.format(row[0]),
                    'bill_type' : row[1],
                    'register_timestamp' : row[2],
                    'due_timestamp' : row[3],
                    'value' : '{}'.format(row[4]),
                    'code' : row[5],
                    'resident' : row[6]
                }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when get bills"
            }

    def get_bills_list_sql(self):
        sql = """
        select
            id, bill_type, register_timestamp, due_timestamp, value, code, resident
        from 
            organizzare_app.bills b
        """
        return sql
    
    def list_bils(self):
        trans = self.conn.begin()
        sql_list = self.get_bills_list_sql()
        try:
            result = self.conn.execute(sql_list)
            trans.commit()
            bill=[]
            for row in result:
                bills={
                    'id' : '{}'.format(row[0]),
                    'bill_type' : row[1],
                    'register_timestamp' : row[2],
                    'due_timestamp' : row[3],
                    'value' : '{}'.format(row[4]),
                    'code' : row[5],
                    'resident' : row[6]
                }
                bill.append(bills)
            return {
                'bill': bills
            }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when list bills"
            }

    def get_bills_from_residents_sql(self, residents_id):
        sql = """
        select
            id, bill_type, register_timestamp, due_timestamp, value, code, resident
        from
            organizzare_app.bills b
        where
            b.resident='{}'
        """.format(residents_id)
        return sql
    
    def list_bils_from_residents(self, residents_id):
        trans = self.conn.begin()
        sql_list = self.get_bills_from_residents_sql(residents_id)
        try:
            result = self.conn.execute(sql_list)
            trans.commit()
            bill=[]
            for row in result:
                bills={
                    'id' : '{}'.format(row[0]),
                    'bill_type' : row[1],
                    'register_timestamp' : row[2],
                    'due_timestamp' : row[3],
                    'value' : '{}'.format(row[4]),
                    'code' : row[5],
                    'resident' : row[6]
                }
                bill.append(bills)
            return {
                'bill': bills
            }
        except:
            print_exc()
            trans.rollback()
            return {
                "message": "error happened when list bills"
            }

