def create_residents(name, cpf, register_timestamp, unregister_timestamp, apartment_id, foreign, primary):
    sql = """
    insert into organizzare_app.condominium(id, name, cpf, register_timestamp, unregister_timestamp, apartment_id, foreign, primary)
    values(uuid_generate_v4(),{},{},{},{},{},{},{})
    """.format(name, cpf, register_timestamp, unregister_timestamp, apartment_id, foreign, primary)
    return sql
    