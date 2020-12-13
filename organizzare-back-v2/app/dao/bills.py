def create_bills(bill_type, register_timestamp, due_timestamp, value, code, resident, foreign, primary):
    sql = """
    insert into organizzare_app.condominium(id, bill_type, register_timestamp, due_timestamp, value, code, resident, foreign, primary)
    values(uuid_generate_v4(),{},{},{},{},{},{},{},{})
    """.format(bill_type, register_timestamp, due_timestamp, value, code, resident, foreign, primary)
    return sql
    