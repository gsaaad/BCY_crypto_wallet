from pymongo import MongoClient
client = MongoClient('mongodb+srv://gsaaad:mongodjango@cluster0.4yjqtsv.mongodb.net/?retryWrites=true&w=majority', 27017)

#database is miWallets
db = client['miWallets']
# collection Wallets
Wallets = db['Wallets']
# collection Users
Users = db['Users']
print("CLIENT",client)
print("WALLETS, ", Wallets)
print("USERS: ", Users)

user1 = {"name": "John", "email": "johndoe123@gmail.com", "password": "test123", "walletID":1}
user2 = {"name": "mike", "email": "mike123@gmail.com", "password": "test123" , "walletID":2}
user3 = {"name": "steve", "email": "steve123@gmail.com", "password": "test123" , "walletID":3}
user4 = {"name": "michelle", "email": "michelle123@gmail.com", "password": "test123" , "walletID":4}
user5 = {"name": "aurora", "email": "aurora123@gmail.com", "password": "test123" , "walletID":5}

Users.insert_many(
    [user1, user2, user3, user4, user5]
)

#wallets collection wallet, public private and WIF

wallet1 = {"_id":1,"address": "Buczw27JdT62e1JrjTdkDaJp2uo1YPam4y", "public": "03917f2203701423c35e037370db6868fd705a71085ae0ca48af87fd6591476255", "private":"251251f39d3d7fa723f98ec56a55978dbafd36984b6c9610dd050317ceab06b","wif":"Bpa6MGjhLkeUWBx7NyX1C6xCkbU3eguiiy44k88K1ASbqZKocepg"}
wallet2 = {"_id":2,"address": "BwiZE2Yfxyeuf9EuTbzhv1tXUZLfGUPbB8", "public": "0316f62484492171112ed0419bcb136bf810328afb7ed63da47b0cc073fc4aee10", "private":"51a5c77f907af1315fb02471a96dc8c68bd97135d1337a71cc909a80661b87e2","wif":"Br4k3gSHBmUXzQ6AP8FVRLGCRjHBn4ypSUYpYTKAfiXSRwsi9KGH"}
wallet3 = {"_id":3,"address": "C1EZF2bZ3ybW6i5rijoB4stKeZp3cv2XJT", "public": "03471228ed81bfd638373efd4e57ee056b27ea80141a5fc04f3a33d5a17e13d652", "private":"146e5f1fe9c19208b005fdc7d231576588d8bf3f5304f3616d3c6f6c900a884c","wif":"Bp1kEbzJpVdrDi6sfNPCvScre4JxBE9rbMV4xxWJAmxQq4Umdpqj"}
wallet4 = {"_id":4,"address": "C6ZBNon8eM4kVYpWHA63V8GU942HvRusUn", "public": "02c3ceba4b22d32a201dae440e35dd7425fb54a47920d75da57b7a3e6c13f27881", "private":"76d036e0485822c03856b8eea257398f4f19330f5d0fd00f4feff353a1ba9d89", "wif":"BsJzH9wFVwJZdhmS7R2ki5UeX4vaK2Bnofc48pWK39yWwGVe1bzf"}
wallet5 = {"_id":5,"address": "CF4MeJWQTvEZQA45uesypmSAFUhjYASjzD", "public":"03a1c4c45f8c4a847c520f46bc4970522aac0605022e0aeb266f9b6be4bad41c74", "private": "9e6a8ff7f22b37faaf9495c1409c6d6a7f754f5a0e5c046fe0811d33a3323925", "wif":"BtdyHeXhnf2Q8iALJxvWX5dtdGJSutzYAUx7yGnzjqCHbZTVUryW"}

Wallets.insert_many([wallet1,wallet2,wallet3,wallet4,wallet5])
print("ALL COLLECTIONS", db.list_collection_names())




