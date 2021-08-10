import librosa
import pydub
import numpy as np


SAMPLE_RATE = 44100


def audioRead(path):
    # 한 함수에 기능이 3개 정도 됨(파일 읽기, 채널 줄이기, 다운샘플링하기) -> 세 개로 쪼갤 필요성
    ext = path.split(".")[-1]
    if ext == "wav" or ext == "flac" or ext == "ogg":
        y, sr = librosa.load(path, sr=SAMPLE_RATE, mono=True)
        return y, sr
    elif ext == "mp3" or ext == "m4a":
        if ext == "mp3":
            a = pydub.AudioSegment.from_mp3(path)
        else:
            a = pydub.AudioSegment.from_file(path)
        y = np.array(a.get_array_of_samples(), dtype=np.float32) / 2 ** 15

        if a.channels == 2:
            y = y.reshape((-1, 2))
            y1 = y[:, 0]
            y2 = y[:, 1]
            # 일단 스테레오면 왼쪽 음원만 활용 (평균 x)
            y = y1  # (y1 + y2) / 2

        if a.frame_rate < SAMPLE_RATE:
            return "e1"
        elif a.frame_rate > SAMPLE_RATE:
            resample = librosa.resample(y, a.frame_rate, SAMPLE_RATE)
            y, a.frame_rate = resample, SAMPLE_RATE

        return y, a.frame_rate
    else:
        return "e2"
