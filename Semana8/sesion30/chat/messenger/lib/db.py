import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("chat-codigo6-3c435-firebase-adminsdk-kixx0-7e2587c46c.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
#database = db.reference('mensaje')
#datos = ref.get()