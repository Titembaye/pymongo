#importation des packages et modules
import pymongo


#on peut se conneter à MongoDB de plusieurs manières
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient = pymongo.MongoClient(host="localhost",port=27017)

