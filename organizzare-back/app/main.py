from controllers import app
import os

JWT_PASSWORD = os.environ.get('JWT_PASSWORD')
if JWT_PASSWORD == None:
    os.environ['JWT_PASSWORD'] = 'kh3b423bh342blh4234bl'
    
app.run()
