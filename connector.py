import firebase_admin
from fb_info import cred_path
from pb_info import config
from firebase_admin import credentials
from firebase_admin import firestore
import pyrebase
import os


class GroovleConnector:
    def __init__(self):
        self.dbClient = None
        self.storageClient = None
        self.audioSource = None
        self.roomObj = None
        self.audioSourceIds = []
        self.audioSources = []

    def getClient(self):
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred, {"projectId": "groovle-app"})
        self.dbClient = firestore.client()

        firebaseApp = pyrebase.initialize_app(config)
        self.storageClient = firebaseApp.storage()

    def getOneAudioSource(self, audioSourceId):
        audioSources_ref = self.dbClient.document("audioSources", audioSourceId)
        self.audioSource = audioSources_ref.get().to_dict()
        print(self.audioSource)

    def getAudioSourceIds(self, roomDocumentId):
        rooms_ref = self.dbClient.document("rooms", roomDocumentId)
        self.roomObj = rooms_ref.get().to_dict()
        self.audioSourceIds = self.roomObj["audioSourceIds"]
        if not os.path.isdir("audio/" + self.roomObj["roomId"]):
            os.mkdir("audio/" + self.roomObj["roomId"])

    def getAudioSources(self):
        for audioSourceId in self.audioSourceIds:
            audioSource_ref = self.dbClient.document("audioSources", audioSourceId)
            audioSource = audioSource_ref.get().to_dict()
            self.audioSources.append(audioSource)


if __name__ == "__main__":
    roomDocumentId = "qR4F9iAMdqyQQqPZSHhI"
    connector = GroovleConnector()
    connector.getClient()
    connector.getAudioSourceIds(roomDocumentId)
    connector.getAudioSources()
