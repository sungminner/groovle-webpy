import os


class GroovleSynthesizer:
    # 어차피 나중 되면 GroovleEditor랑 GroovleSynthesizer랑 분리해야 함
    # GroovleEditor는 main이랑은 별개로 웹과
    # 지금은 박자 분석과 합성 둘 다 한다고 생각
    def __init__(self, roomId):
        self.roomId = roomId
        self.paths = os.listdir("audio/" + self.roomId + "/download")
        self.audioSources = []  # audioSource 딕셔너리 저장

    def readAudioSources(self):
        pass

    def beatTrack(self):  # GroovleBeatTracker 따로 만들기?
        pass

    def adjustStartBeat(self):
        pass

    def timeStretch(self):  # GroovleTimeStretcher도 따로 만들기?
        pass

    def synthesize(self):
        pass


if __name__ == "__main__":
    synthesizer = GroovleSynthesizer("igrY")
    synthesizer.readAudioSources()
    print(synthesizer.paths)
    synthesizer.beatTrack()
    synthesizer.timeStretch()
    synthesizer.synthesize()
