def generate_insert_user(name, cpf, data_cadastro):
    sql = """
    INSERT INTO residents (id, name, cpf)
    VALUES (uuid_generate_v4(), {}, {});
    """.format(name, cpf)

    return sql

y = generate_insert_user(data["name"], data["cpf"], data["date"])
print(y)

