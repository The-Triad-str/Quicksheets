import librosa
import numpy as np
import pygame
import matplotlib.pyplot as plt
import playback as m

group = []
music, sr = librosa.load("/Users/snehal/PycharmProjects/quicksheet2/backend/sonatina_for_solo_flute.wav")
music = librosa.resample(music, orig_sr=sr, target_sr=11000)
sr = 11000

f = open("pitches.txt", "w")


def detect_pitch(magnitudes, pitches, t):
    index = magnitudes[:, t].argmax()
    pitch = pitches[index, t]
    return pitch


def detect_frame(arr, bin):
    # freq smoothing
    fs = 0.026
    notes = []
    notesfi = []
    # bin freqs into list
    for i in range(0, len(arr), bin):
        if i + bin <= len(arr):
            av = np.average(arr[i:i + bin])
            notes.append((av, bin))
    num_of_change = 1

    # Combine similar notes into one
    while (num_of_change > 0):
        i = 0
        num_of_change = 0
        while i < len(notes):
            if i + 1 != len(notes):
                error = fs * notes[i][0]
                if (notes[i + 1][0] < error + notes[i][0]) and (notes[i + 1][0] > notes[i][0] - error):
                    val_of_both = (notes[i][0] + notes[i + 1][0]) / 2
                    notesfi.append([val_of_both, notes[i][1] + notes[i + 1][1]])
                    i = i + 1
                    num_of_change = num_of_change + 1
                else:
                    notesfi.append([notes[i][0], notes[i][1]])
            else:
                notesfi.append([notes[i][0], notes[i][1]])
            i = i + 1
        notes = notesfi
        notesfi = []
    return notes


def getn():
    pitches, magnitudes = librosa.piptrack(y=music, sr=sr, fmin=200, fmax=2500, n_fft=512)

    # print(np.shape(pitches))
    # magnitudes = magnitudes.transpose()
    # pitches = pitches.transpose()

    # gets pitches at given second
    a = 0
    for i in range(len(pitches[0])):
        # print(i * 0.023585)
        # print(detect_pitch(magnitudes, pitches, i))
        if detect_pitch(magnitudes, pitches, i) == 0:
            a = a + 1
        n = str(detect_pitch(magnitudes, pitches, i))
        group.append(float(n))

    complete_notes = detect_frame(group, 10)
    print(complete_notes)
    return complete_notes

if __name__ == "__main__":
    # playback
    sampleRate = 44100
    bits = 16

    # initializing pygame mixer
    pygame.mixer.pre_init(44100, -bits, 2)
    pygame.init()

    arr_to_play = []
    complete_notes = getn()
    for i in complete_notes:
        arr_to_play = arr_to_play + m.createSound(sampleRate, i[0], bits, i[1] * 0.015).tolist()
    play_te = pygame.sndarray.make_sound(np.array(arr_to_play, dtype="int16"))
    play_te.play(loops=1)
    pygame.time.delay(int(20000))
    play_te.stop()

"""
# write edited pitches into file
for i in group:
    f.write(str(i) + "\n")

f.close()

# get time axis
times = []
for num, i in enumerate(group):
    times.append(librosa.frames_to_time(num, sr=sr))


plt.scatter(times[10:2000], group[10:2000])
plt.show()


'''
i=0
while i < range(len(music)):
    if i
print(group)

plt.plot(group)
plt.show()

'''
"""
