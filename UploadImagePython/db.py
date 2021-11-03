from flask_pymongo import PyMongo
from pymongo import MongoClient
import server as s

s.app.config['MONGO_DBNAME'] = 'MVision'
s.app.config['MONGO_URI'] = 'mongodb://localhost:27017/MVision'
mongo = PyMongo(s.app)

