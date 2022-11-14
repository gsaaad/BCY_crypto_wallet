from pymongo import MongoClient
client = MongoClient('mongodb+srv://gsaaad:mongodjango@cluster0.4yjqtsv.mongodb.net/?retryWrites=true&w=majority', 27017)

db = client['AllWallets']
collection = db['miWallet']
print(client)

post = {"_id: ": 0, "name": "George", "wallet":"walletID"}
collection.insert_one(post)