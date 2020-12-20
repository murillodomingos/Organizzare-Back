from dao import get_connection
from dao.admins import Admins_DAO
from datetime import datetime, timedelta
from passlib.hash import pbkdf2_sha256
import jwt
import os

class Admins_Service():
    def __init__(self):
        conn = get_connection()
        self.admins_DAO = Admins_DAO(conn)

    def create_admins(self, name, phone, cpf, user_type, user_pass):
        try:
            register_timestamp = datetime.now().isoformat()
            user_hash = pbkdf2_sha256.hash(user_pass)
            obj = self.admins_DAO.create_admins(name, phone, cpf, register_timestamp, user_type, user_hash)
            return obj
        except Exception as err:
            return {
                'message': "{}".format(err)
            }

    def update_admins(self, id, name, phone, cpf, user_type):
        try:
            obj = self.admins_DAO.update_admins(id, name, phone, cpf, user_type)
            return obj
        except Exception as err:
            return {
                'message': "{}".format(err)
            }

    def get_admins(self, id):
        try:
            return_obj = self.admins_DAO.get_admins(id)
            return return_obj
        except Exception as err:
            return {
                'message': "{}".format(err)
            }

    def list_admins(self):
        try:
            result = self.admins_DAO.list_admins()
            return result
        except Exception as err:
            return {
                'message': "{}".format(err)
            }

    def create_admins_condomoniums(self, admins_id, condominium_id):
        try:
            return self.admins_DAO.create_admins_condomoniums(admins_id, condominium_id)
        except Exception as err:
            return {
                'message': "{}".format(err)
            }

    def get_admin_condominium(self, cpf):
        try:
            return self.admins_DAO.get_admin_condominium(cpf)
        except Exception as err:
            return {
                'message': "{}".format(err)
            }

    def get_jwt(self, admin_id, user_type):
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=0, seconds=100000),
                'iat': datetime.utcnow(),
                'sub': admin_id,
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

    def admin_signin(self, cpf, user_pass):
        try:
            admin = self.admins_DAO.get_hash_from_admin(cpf)
            get_hash = admin['hash']
            admin_id = admin['id']
            user_type = admin['user_type']
            verify = pbkdf2_sha256.verify(user_pass, get_hash) 
            if verify == True:
                return {
                    'message':'CORRECT PASS',
                    'token': self.get_jwt(admin_id, user_type).decode('ascii')
                }
            return {
                'message':'WRONG PASS'
            }
        except Exception as err:
            return {
                'message': "{}".format(err)
            }
