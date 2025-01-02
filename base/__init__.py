from datetime import timedelta
import warnings
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '78BCAEE361BF7'

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3307/news_website'

app.config['SQLALCHEMY_ECHO'] = False

app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

db = SQLAlchemy(app)

from base.com import controller