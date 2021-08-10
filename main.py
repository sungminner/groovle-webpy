import sys
from connector import GroovleConnector


class Groovle:
    def __init__(self):
        self.connector = GroovleConnector()
        self.roomDocumentId = ""

    def getRoomDocumentId(self):
        self.roomDocumentId = sys.argv[1]
        print(self.roomDocumentId)

    def connect(self):
        self.connector.getClient()
        self.connector.getAudioSourceIds(self.roomDocumentId)
        self.connector.getAudioSources()
        self.connector.readAudioSources()
        print("connected!!!")

groovle = Groovle()
groovle.getRoomDocumentId()
groovle.connect()