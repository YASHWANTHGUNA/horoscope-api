from flask import Flask
from decouple import config
from flask_restx import Api
from flask_caching import Cache

# Initialize extensions first
cache = Cache()


# Create App
app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

# Link extensions to the app
cache.init_app(app)

api = Api(
         app,
         version='1.0',
         description='Get your horoscope data easily using the below APIS',
        
         contact='ROCKY',
         contact_url='https://rocky.com',
         contact_email='hyderabadiyash@gmail.com',
         doc='/',
         prefix='/api/v1'
)

   

# Import routes after app and extensions are configured
from core import routes