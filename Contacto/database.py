from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://denismembrive:12345@cluster0.ufacn2z.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
