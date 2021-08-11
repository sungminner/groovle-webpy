import soundfile as sf
import io
import numpy as np

from urllib.request import urlopen

import pydub
import librosa

from scipy.io.wavfile import write

SAMPLE_RATE = 44100


def audioRead(url, ext):
    if ext == "wav" or ext == "flac" or ext == "ogg":
        y, sr = sf.read(io.BytesIO(urlopen(url).read()))
        ch_len = len(np.shape(y))

    elif ext == "mp3" or ext == "m4a":
        # 일단 tmp로 저장하고 pydub로 열어서 출력
        file = urlopen(url)
        with open("./audio/tmp/tmp." + ext, "wb") as output:
            output.write(file.read())

        if ext == "mp3":
            a = pydub.AudioSegment.from_mp3("./audio/tmp/tmp.mp3")
        else:
            a = pydub.AudioSegment.from_file("./audio/tmp/tmp.m4a")
        y = np.array(a.get_array_of_samples(), dtype=np.float32) / 2 ** 15
        sr = a.frame_rate
        ch_len = a.channels
        # mp3, m4a dtype이 뭔지 확인

    else:
        return "error"

    if ch_len == 2:
        y = y.reshape((-1, 2))
        y1 = y[:, 0]
        # y2 = y[:, 1]
        # 일단 스테레오면 왼쪽 음원만 활용 (평균 x)
        y = y1  # (y1 + y2) / 2

    if sr != SAMPLE_RATE:
        y = librosa.resample(y, sr, SAMPLE_RATE)
        sr = SAMPLE_RATE

    return y, sr


if __name__ == "__main__":
    url = "https://firebasestorage.googleapis.com/v0/b/groovle-app.appspot.com/o/Cb6LSQg9mahHeEVwvUqvPUoZ3So2%2F826bd7c2-6552-4d35-b394-579ab6b9afb8.m4a?alt=media&token=1bf94e42-f9d6-496b-aff7-ddb677473212"
    ext = "m4a"

    y, sr = audioRead(url, ext)
    write("audio/igrY/result/result.wav", 44100, y)
