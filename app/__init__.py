from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
import os


app = Flask(__name__)
app.config.from_object(Config)

# db = our database
db = SQLAlchemy(app)
# migration engine
migrate = Migrate(app, db)

boostrap = Bootstrap(app)

from app import routes
