# import soundfile as sf
# import io
# import numpy as np

# from urllib.request import urlopen
# from scipy.io.wavfile import write

# url = "https://firebasestorage.googleapis.com/v0/b/groovle-app.appspot.com/o/Cb6LSQg9mahHeEVwvUqvPUoZ3So2%2F266299bf-d7fd-4136-bf8f-a95dfa07122c?alt=media&token=47ac14c2-24b7-4a0c-9d4c-c3ddedeb854d"
# # data, samplerate = sf.read(io.BytesIO(urlopen(url).read()))
# # data = data.astype(np.float32)
# # print(samplerate)

# file = urlopen(url)
# with open("./audio/plerrrase.mp3", "wb") as output:
#     output.write(file.read())

# print(file.read())


# # write("audio/igrY/result/url_downloaded.wav", samplerate, data)
# # print(type(data))

import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
print(len(np.shape(a)))
