import firebase_admin
from fb_info import cred_path
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred, {"projectId": "groovle-app"})

dbClient = firestore.client()

# doc_ref = db.collection(u"users").document("user02")
# doc_ref.set({u"level": 23, u"money": 701, u"job": "Mage"})

roomDocumentId = "aCs00NPMrnmtJjasluHC"

users_ref = dbClient.document(u"rooms", roomDocumentId)
doc = users_ref.get()
print(doc.to_dict())
