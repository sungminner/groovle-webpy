import firebase_admin
from fb_info import cred_path
from pb_info import config
from firebase_admin import credentials
from firebase_admin import firestore
import pyrebase


class GroovleConnector:
    def __init__(self):
        self.dbClient = None
        self.storageClient = None
        self.roomObj = None
        self.audioSourceIds = []
        self.audioSources = []

    def getClient(self):
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred, {"projectId": "groovle-app"})
        self.dbClient = firestore.client()

        firebaseApp = pyrebase.initialize_app(config)
        self.storageClient = firebaseApp.storage()

    def getAudioSourceIds(self, roomDocumentId):
        rooms_ref = self.dbClient.document("rooms", roomDocumentId)
        self.roomObj = rooms_ref.get().to_dict()
        self.audioSourceIds = self.roomObj["audioSourceIds"]

    def getAudioSources(self):
        for audioSourceId in self.audioSourceIds:
            audioSource_ref = self.dbClient.document("audioSources", audioSourceId)
            audioSource = audioSource_ref.get().to_dict()
            self.audioSources.append(audioSource)
        print(self.audioSources)

    def readAudioSources(self):
        for audioSource in self.audioSources:
            self.storageClient.child().download(
                audioSource["creatorId"]
                + "/"
                + audioSource["audioSourceStorageName"]
                + "."
                + audioSource["extension"],
                "download/"
                + audioSource["belongingRoomSongName"]
                + " - "
                + audioSource["sessionName"]
                + "."
                + audioSource["extension"],
            )


if __name__ == "__main__":
    groovle = GroovleConnector()
    groovle.getClient()
    groovle.getAudioSourceIds()
    groovle.getAudioSources()
    groovle.readAudioSources()
