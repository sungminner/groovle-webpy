import sys
from connector import GroovleConnector
from synthesizer import GroovleSynthesizer


class Groovle:
    def __init__(self):
        self.roomDocumentId = ""
        self.connector = GroovleConnector()
        # self.synthesizer = GroovleSynthesizer()

    def getRoomDocumentId(self):
        self.roomDocumentId = sys.argv[1]
        print(self.roomDocumentId)

    def connect(self):
        self.connector.getClient()
        self.connector.getAudioSourceIds(self.roomDocumentId)
        self.connector.getAudioSources()
        self.connector.downloadAudioSources()
        print("connected!!!")

    def synthesize(self):
        pass


groovle = Groovle()
groovle.getRoomDocumentId()
groovle.connect()
