import librosa
import numpy as np
from scipy.io.wavfile import write
from audioread import audioRead


class AudioFile:
    def __init__(self, path):
        self.path = path
        self.name = path.split("/")[-1].split(".")[0]
        self.bpm = None  # 원곡의 bpm, 이건 곡의 정보...
        self.y = None
        self.sr = None
        self.tempo = None
        self.beat_samples = None
        self.volume = 1

    def fileOpen(self):
        self.y, self.sr = audioRead(self.path)

    def setBpm(self, bpm):
        self.bpm = bpm

    def setVolume(self, v):
        self.volume = v

    def isTracked(self):
        if self.tempo is None:
            return False
        else:
            return True

    def beatTrack(self):
        self.tempo, self.beat_samples = librosa.beat.beat_track(
            self.y, sr=self.sr, start_bpm=self.bpm, units="samples"
        )
        self.beat_samples = np.hstack(
            (np.array([0]), self.beat_samples, np.array([len(self.y) - 1]))
        )
        # TODO: 음악 처음, 마지막 부분 beat track 안될때 어떻게 보정할지

    def saveWithClicks(self):
        beat_times = librosa.samples_to_time(self.beat_samples, sr=self.sr)
        clicks = librosa.clicks(beat_times, sr=self.sr, length=len(self.y))
        result = self.y + clicks
        write("audio/tracked_result/beattrack_" + self.name + ".wav", self.sr, result)

    def adjustStartBeat(self, index):
        # 사용자가 직접 beat track 결과 들어보고 시작 박자 입력하게 하기 (나중에는 gui로도 표시)
        if index >= 3:  # 3보다 작으면 무의미한 실행. 실행 x
            self.y = self.y[self.beat_samples[index - 2] :]
            # 몇 번째 클릭이 시작인지로 입력받으므로, 전 마디까지 보존하기 위해 -2
            self.beat_samples = self.beat_samples - self.beat_samples[index - 2]
            self.beat_samples = self.beat_samples[index - 2 :]

    def timeStretch(self):
        original_samples_per_block = self.sr * 60 / self.bpm
        result = np.array([])
        for i in range(len(self.beat_samples) - 1):
            block = self.y[self.beat_samples[i] : self.beat_samples[i + 1]]
            stretch_ratio = len(block) / original_samples_per_block
            block_str = librosa.effects.time_stretch(block, stretch_ratio)
            result = np.append(result, block_str)
        self.y = result
        # TODO: time stretch를 해도 beat_samples는 변하지 않음. (쓸모가 없어짐) UI를 통해 어디 박자가 첫 박자인지를 먼저 선택하게 하기?


if __name__ == "__main__":
    mypath = input("input path: ")
    mybpm = int(input("input bpm: "))
    myvolume = int(input("input volume:"))

    myfile = AudioFile(mypath)
    myfile.fileOpen()
    myfile.setBpm(mybpm)
    myfile.setVolume(myvolume)
    myfile.beatTrack()
    myfile.saveWithClicks()

    start = int(input("시작하는 박자까지의 클릭 수: "))
    myfile.adjustStartBeat(start)
    myfile.timeStretch()

    print("path: ", myfile.path)
    print("name: ", myfile.name)
    print("bpm: ", myfile.bpm)
    print("y: 생략")
    print("sr: ", myfile.sr)
    print("tempo: ", myfile.tempo)
    print("beat_samples: ", myfile.beat_samples[:5], "...", myfile.beat_samples[-5:])
    print("volume_ratio: ", myfile.volume)

    write(
        "audio/tracked_result/beattrack+timestretched_" + myfile.name + ".wav",
        myfile.sr,
        myfile.y,
    )
