import numpy as np
from scipy.io.wavfile import write
from audiofile import AudioFile

SAMPLE_RATE = 44100


class Merger:
    def __init__(self, filelist):
        self.filelist = filelist
        self.sr = SAMPLE_RATE  # 어떻게 입력받을지 생각
        # 박자분석, time stretch 등등 다 된 filelist가 들어온다고 가정
        # filelist는 사용자가 path list를 주면 그걸 filelist로 사용

    def matchLength(self):
        max_len = 0
        for audiofile in self.filelist:
            if len(audiofile.y) > max_len:
                max_len = len(audiofile.y)
        for audiofile in self.filelist:
            padding = np.zeros(max_len - len(audiofile.y))
            audiofile.y = np.hstack((audiofile.y, padding))

    def volumeAdjust(self):
        for audiofile in self.filelist:
            audiofile.y = audiofile.y * audiofile.volume

    def merge(self):
        merged = 0
        for audiofile in self.filelist:
            merged = merged + audiofile.y
        merged = merged / len(self.filelist)
        # 각 y에 볼륨값 곱하고 총 볼륨으로 나누기 (볼륨 0~100을 0~1로 바꿔서)
        merged32 = merged.astype(np.float32)
        return merged32


if __name__ == "__main__":
    mylist = []
    while True:
        print("=" * 10, "Groovle Merger", "=" * 10)
        print("1. 음원 파일 추가")
        print("2. 박자 분석")
        print("3. 합성")
        selected = input("메뉴 번호를 입력하세요: ")

        if selected == "1":
            mypath = input("path: ")
            myvolume = float(input("input volume: "))

            myfile = AudioFile(mypath)
            myfile.fileOpen()
            myfile.setVolume(myvolume)
            mylist.append(myfile)
            print("음원이 추가되었습니다.\n")
            for afile in mylist:
                print(afile.name, "volume:", afile.volume)

        elif selected == "2":
            bpm = input("원곡 bpm: ")
            beatlist = []
            for i in range(len(mylist)):
                print(mylist[i].name)
                beatlist.append(int(input("시작하는 박자까지의 클릭 수: ")))
            for i in range(len(mylist)):
                mylist[i].setBpm(int(bpm))
                mylist[i].beatTrack()
                mylist[i].saveWithClicks()
                print(mylist[i].name)
                start = beatlist[i]
                mylist[i].adjustStartBeat(start)
                mylist[i].timeStretch()

        elif selected == "3":
            mymerger = Merger(mylist)
            mymerger.matchLength()
            mymerger.volumeAdjust()
            result = mymerger.merge()
            write("audio/merged_result/merged_result.wav", mymerger.sr, result)
            break
