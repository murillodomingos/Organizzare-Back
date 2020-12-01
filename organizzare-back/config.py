DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s'%('organizzare-user','organizzare-pass','localhost','5432','organizzare')
SQLALCHEMY_TRACK_MODIFICATIONS = True