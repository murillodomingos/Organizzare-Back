from werkzeug.wrappers import Request, Response, ResponseStream
from service.admins import Admins_Service
import jwt
from traceback import print_exc

class middleware():

    def __init__(self, app):
        self.app = app
        self.admins_service = Admins_Service()

    def __call__(self, environ, start_response):
        request = Request(environ)
        print(request.full_path)
        if request.full_path == '/admins/signin?': 
            return self.app(environ, start_response)
        
        if request.full_path == ('/residents/signin?'):
            return self.app(environ, start_response)

        try:
            if 'jwt' in request.headers:
                admin_jwt = request.headers['jwt']
                if self.get_user_authentication(admin_jwt) == 'admin':
                    return self.app(environ, start_response)
                if self.get_user_authentication(admin_jwt) == 'resident' and request.full_path.startswith('/bills') and request.method == 'GET':
                    return self.app(environ, start_response)
        except:
            print_exc()
            print("error happened, returning fail")
        res = Response(u'Authorization failed', mimetype= 'text/plain', status=401)
        return res(environ, start_response)


    def get_user_authentication(self, user_jwt):    
        try:
            payload = jwt.decode(user_jwt, 'j4g2373gda3g3')
            return payload['user_type']
        except jwt.ExpiredSignatureError:
            raise 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            raise 'Invalid token. Please log in again.'