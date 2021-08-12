import sys
from connector import GroovleConnector
from synthesizer import GroovleSynthesizer


class Groovle:
    def __init__(self):
        self.audioSources = []
        self.connector = GroovleConnector()
        self.synthesizer = GroovleSynthesizer()

    # 편집
    def audioConnect(self):
        self.connector.getClient()
        self.connector.getOneAudioSource(sys.argv[2])
        self.audioSource = self.connector.audioSource
        print("edit connected!!!")

    def edit(self):
        pass

    # 합성
    def roomConnect(self):
        self.connector.getClient()
        self.connector.getAudioSourceIds(sys.argv[2])
        self.connector.getAudioSources()
        self.audioSources = self.connector.audioSources
        print("synthesize connected!!!")

    def synthesize(self):
        self.synthesizer.setAudioSources(self.audioSources)
        self.synthesizer.synthesize()
        self.synthesizer.saveAsFile()


groovle = Groovle()
if sys.argv[1] == "edit":
    groovle.audioConnect()
    # groovle.edit()
elif sys.argv[1] == "synthesize":
    groovle.roomConnect()
    groovle.synthesize()
