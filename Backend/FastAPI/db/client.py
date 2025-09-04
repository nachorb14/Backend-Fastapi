from pymongo import MongoClient

# Base datos local
# db_client = MongoClient().local

# Base de datos remota
db_client = MongoClient("mongodb+srv://Test:Test@cluster1.fijl8rj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1").test