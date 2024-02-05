#importation des packages et modules
from connection import myclient


#création d'une base de données
mydb = myclient["mydatabase"]


#verifier la liste des bases de données
#print(myclient.list_database_names())