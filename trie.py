#importation des packages et modules
from collection import mycol


clients = mycol.find().sort("name")
for client in clients:
    print(client)