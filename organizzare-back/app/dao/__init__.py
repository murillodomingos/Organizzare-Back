from sqlalchemy import create_engine

def get_connection():
    engine = create_engine('postgresql://organizzare-user:organizzare-pass@localhost:5432/organizzare')

    return engine.connect()
    