from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

import controllers.apartments
import controllers.bills
import controllers.condominium
import controllers.residents