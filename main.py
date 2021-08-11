import sys
from connector import GroovleConnector
from synthesizer import GroovleSynthesizer


class Groovle:
    def __init__(self):
        self.roomDocumentId = sys.argv[1]
        self.audioSources = []
        self.connector = GroovleConnector()
        self.synthesizer = GroovleSynthesizer()
        print(self.roomDocumentId)

    def connect(self):
        self.connector.getClient()
        self.connector.getAudioSourceIds(self.roomDocumentId)
        self.connector.getAudioSources()
        self.audioSources = self.connector.audioSources
        print("connected!!!")

    def synthesize(self):
        self.synthesizer.setAudioSources(self.audioSources)
        self.synthesizer.synthesize()
        self.synthesizer.saveAsFile()


groovle = Groovle()
groovle.connect()
groovle.synthesize()
