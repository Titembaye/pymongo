#importation des packages et modules

from connection import myclient
from database import mydb

#creer une collection
mycol = mydb["customers"]

#verifier la liste des collections
#print(mydb.list_collection_names())
