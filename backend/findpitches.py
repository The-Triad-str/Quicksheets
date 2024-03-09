import librosa
import numpy as np
import matplotlib.pyplot as plt
group = []
music, sr = librosa.load("/Users/snehal/Downloads/aquarium-2.wav")
music = librosa.resample(music, orig_sr=sr, target_sr=11000)

f = open("pitches.txt", "w")

# get avg pitch

def detect_pitch(magnitudes,pitches, t):
    index = magnitudes[:, t].argmax()
    pitch = pitches[index, t]
    return pitch


pitches, magnitudes = librosa.piptrack(y=music, sr=sr, fmin=250, fmax=2500, n_fft=512)
print(np.shape(pitches))

# magnitudes = magnitudes.transpose()
# pitches = pitches.transpose()

# gets pitches at given second
a = 0
for i in range(len(pitches [0])):
    print(i * 0.04717)
    print(detect_pitch(magnitudes, pitches, i))
    if detect_pitch(magnitudes, pitches, i) == 0:
        a = a +1
    n = str(detect_pitch(magnitudes, pitches, i))
    group.append(float(n))



print(a)
print(len(pitches[0]))

# calculate avg pitch
'''
sum = 0
for i in group:
    sum = sum + i
'''

avg = np.median(group)
print(avg)


def sigmoid(pitch):
    global avg
    denom = 1 + (2.7183 ** (-0.008 * (float(pitch) - avg)))
    fi = (382.5/ denom) - 127.5
    return fi/255


# write edited pitches into file
for i in group:
    f.write(str(sigmoid(i)) + "\n")

f.close()

'''
with open("pitchavg.txt", "w") as f:
    f.write(str(avg) + "\n")
'''

plt.plot(pitches)
plt.show()


'''
i=0
while i < range(len(music)):
    if i
print(group)

plt.plot(group)
plt.show()

'''
