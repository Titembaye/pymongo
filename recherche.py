#importation des packages et modules
from collection import mycol


#recuperer le premier document
first_client = mycol.find_one()
#print(first_client)

#rechercher plusieurs documents et afficher certains champs uniquement
clients=mycol.find({},{"name":True})
#for client in clients:
    #print(client)


query_by_address = { "address": "Park Lane 38" }

#clients = mycol.find(query_by_address)
#for client in clients:
    #print(client)

#myquery = { "address": { "$gt": "S" } }
myquery = { "address": { "$regex": "^S" } }
mydoc = mycol.find(myquery)
for cl in mydoc:
    print(cl)
