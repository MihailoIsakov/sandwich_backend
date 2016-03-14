from flask import Flask
from pymongo import MongoClient

client = MongoClient()

# dbs
blic = client.blic
b92 = client.b92

app = Flask(__name__)
from sandwich_backend import views

if __name__ == '__main__':
    app.run()
