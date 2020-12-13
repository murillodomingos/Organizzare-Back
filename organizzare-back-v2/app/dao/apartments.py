def create_apatments(number, block, condominium):
    sql = """
    insert into organizzare_app.condominium(id, number, block, condominium)
    values(uuid_generate_v4(),{},{},{})
    """.format(number, block, condominium)
    return sql
