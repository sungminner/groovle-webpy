import numpy as np
from audioread import audioRead
from scipy.io.wavfile import write


class GroovleSynthesizer:
    # 어차피 나중 되면 GroovleEditor랑 GroovleSynthesizer랑 분리해야 함
    # 지금은 url의 파일이 박자 분석이 완료된 파일이라고 생각
    def __init__(self):
        self.audioSources = []  # audioSource 딕셔너리 저장
        self.result = None

    def setAudioSources(self, list):
        self.audioSources = list

    def synthesize(self):
        result = np.array([])
        for audioSource in self.audioSources:
            y, _ = audioRead(audioSource["audioSourceUrl"], audioSource["extension"])
            if len(result) < len(y):
                temp = y
                temp[: len(result)] += result
            else:
                temp = result
                temp[: len(y)] += y
            result = temp
        result /= len(self.audioSources)
        result = result.astype(np.float32)
        self.result = result

    # 임시로 확인하는 용도. 웹에 연결할 때는 connector 통해 firestore/storage에 업로드
    def saveAsFile(self):
        write(
            "audio/" + self.audioSources[0]["belongingRoomId"] + "/result.wav",
            44100,
            self.result,
        )


if __name__ == "__main__":
    synthesizer = GroovleSynthesizer()
    synthesizer.synthesize()
    synthesizer.saveAsFile()
