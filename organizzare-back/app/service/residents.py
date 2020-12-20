from dao import get_connection
from dao.residents import Residents_DAO
from datetime import datetime, timedelta
from passlib.hash import pbkdf2_sha256
import jwt
import os

class Residents_Service():
    def __init__(self):
        conn = get_connection()
        self.residents_DAO = Residents_DAO(conn)

    def create_residents(self, name, cpf, resident_pass, apartment_id):
        resident_hash = pbkdf2_sha256.hash(resident_pass)
        register_timestamp = datetime.now().isoformat()
        obj = self.residents_DAO.create_residents(name, cpf, register_timestamp, resident_hash, apartment_id)
        return obj

    def update_residents(self, id, name, cpf, apartment_id):
        obj = self.residents_DAO.update_residents(id, name, cpf, apartment_id)
        return obj
    
    def get_residents(self, id):
        return_obj = self.residents_DAO.get_residents(id)
        return return_obj
    
    def list_residents(self):
        result = self.residents_DAO.list_residents()
        return result

    def get_residents_from_apartments(self, condominium_id):
        return self.residents_DAO.list_residents_from_apartments(condominium_id)

    def get_jwt(self, resident_id):
        user_type = 'resident'
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=0, seconds=100000),
                'iat': datetime.utcnow(),
                'sub': resident_id,
                'user_type': user_type
            }
            JWT_PASSWORD = os.environ.get('JWT_PASSWORD')
            return jwt.encode(
                payload,
                JWT_PASSWORD,
                algorithm='HS256'
            )
        except Exception as e:
            return e
    
    def residents_signin(self, cpf, resident_pass):
        try:
            resident = self.residents_DAO.get_hash_from_residents(cpf)
            get_hash = resident['hash']
            resident_id = resident['id']
            verify = pbkdf2_sha256.verify(resident_pass, get_hash) 
            if verify == True:
                return {
                    'message':'CORRECT PASS',
                    'jwt': self.get_jwt(resident_id).decode('ascii')
                }
            return {
                'message':'WRONG PASS'
            }
        except Exception as err:
            return {
                'message': "{}".format(err)
            }
