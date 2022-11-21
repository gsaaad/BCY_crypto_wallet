from pymongo import MongoClient
#pymongo and mongo client
client = MongoClient('mongodb+srv://gsaaad:mongodjango@cluster0.4yjqtsv.mongodb.net/?retryWrites=true&w=majority', 27017)
    

database_name = 'miWallets'

#database is miWallets
db = client[database_name]
# collection Users
Users = db['Users']
# User data: id, first_name, last_name, email, password, Date Of Birth, and Wallet empty list (until they register/create wallet)

# collection Wallets
Wallets = db['Wallets']
#Wallets data: contains all wallets. wallets are objects containing id, address, public, private, wif and associated email.

# collection  OAP
Oap = db['Oap']


if db.list_collection_names():
    print("ALL COLLECTIONS in {} Database".format(database_name), db.list_collection_names())
    print("Connection established to MongoDB database!")




