#importation des packages et modules
from collection import mycol

request={'address':'Ocean blvd 2'}
deleted=mycol.delete_one(request)


myquery = { "address": {"$regex": "^S"} }
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")


print(deleted)