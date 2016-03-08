from flask import Flask
from pymongo import MongoClient

client = MongoClient()
db = client.blic
comments = db.comments
reactions = db.reactions

app = Flask(__name__)
from sandwich_backend import views

if __name__ == '__main__':
    app.run()
