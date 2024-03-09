import sounddevice as sd
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import math
import librosa
import numpy as np

temp = []
f = open("hi.txt", "w")

'''
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
'''

# load piece
music, sr = librosa.load("/Users/snehal/Downloads/aquarium-2.wav")
music = librosa.resample(music, orig_sr=sr, target_sr=2400)

print(len(music))

# find amplitude using log scale every 100 samples
for i in range(0, len(music), 100):
    #print(i/100)
    lis = music[i : i+100]
    for j in range(len(lis)):
        if lis[j] < 0:
            lis[j] = lis[j] * -1
        lis[j] = math.log(lis[j] + 1, 2)
    a = np.max(lis)
    temp.append(a)


for i in temp:
    print(i)
    f.write(str(i)+"\n")
f.close()
'''
for i in music:
    if i < 0:
        i[0] = i[0] * -1
    i[0] = math.log(i[0] + 1, 2)
    f.write(str(i[0]) + "\n")
'''

plt.plot(temp)
plt.show()
