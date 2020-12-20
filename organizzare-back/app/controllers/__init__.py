from flask import Flask
from controllers.middleware import middleware
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.url_map.strict_slashes = False
app.wsgi_app = middleware(app.wsgi_app)

import controllers.admins
import controllers.apartments
import controllers.bills
import controllers.condominium
import controllers.residents