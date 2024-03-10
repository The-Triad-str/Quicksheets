import numpy as np
import pygame
import math
import matplotlib.pyplot as plt


# produces a single value during the sine wave
def soundWave(t, dur, attack, decay, release):
    amp = 1
    if t < attack:
        amp = math.log((t * 10 / attack)+1, 10) - 0.05
    if t >= attack and dur - t >= release:
        amp = 0.0625 * (16 ** (((dur - t) / release) / ((dur - attack) / release)))
    if dur - t <= release:
        amp = (dur - t) / release * 0.0625
    return amp


def expup(t, dur):
    amp = (1 ** (t/dur))
    if amp > 1 - 0.001:
        amp = amp - (amp - 1)
    return amp


def logup(t, dur):
    amp = math.log((t/dur + 1), 2)
    if amp > 1 - .001:
       amp = amp - (amp - 1)
    return amp


def powup(t, dur):
    amp = (-1 * (((t/dur) * 2) - 1) ** 2) + 1
    if amp > 1 - .001:
        amp = amp - (amp - 1)
    return amp


def createSound(sampleRate, freq, bits, duration, attack=.0625, delay=0.49, release=0.01):
    maxSample = 2 ** (bits - 1) - 1
    samples = int(round(duration * sampleRate))

    # initializing numpy array
    arr = np.zeros((samples, 2), dtype=np.int16)

    # creating a numpy array of values
    for i in range(samples):
        t = i / sampleRate
        amp1 = soundWave(t, duration, attack, delay, release) * maxSample
        amp2 = soundWave(t, duration, attack, delay, release) * maxSample
        freq1 = freq + math.sin(2 * math.pi * freq / 100 * t) / 5000 * freq
        freq2 = freq + math.sin(2 * math.pi * freq / 100 * t) / 5000 * freq
        freq2 = freq2
        arr[i][0] = int(round(amp1 * math.sin(2 * math.pi * freq1 * t)) / 2 + round(amp1 * math.sin(2 * math.pi * freq1 / 100 * t)) / 10)
        arr[i][1] = int(round(amp2 * math.sin(2 * math.pi * freq2 * t)) / 2 + round(amp2 * math.sin(2 * math.pi * freq2 / 100 * t)) / 10)

    return arr


if __name__ == "__main__":
    # setting parameters
    sampleRate = 44100
    bits = 16
    duration = .5

    # initializing pygame mixer
    pygame.mixer.pre_init(44100, -bits, 2)
    pygame.init()

    # create sound objects for every note do this, and multiply duration by any value

    C5arr = createSound(sampleRate, 523, bits, duration)
    C5 = pygame.sndarray.make_sound(C5arr)

    G4arr = createSound(sampleRate, 391.995, bits, duration, delay=0.00625, attack=0.00625)
    G4 = pygame.sndarray.make_sound(G4arr)

    As4arr = createSound(sampleRate, 466.14, bits, duration * 0.8)
    As4 = pygame.sndarray.make_sound(As4arr)

    F4arr = createSound(sampleRate, 349.23, bits, duration * 0.8)
    F4 = pygame.sndarray.make_sound(F4arr)

    Fs4arr = createSound(sampleRate, 369.99, bits, duration)
    Fs4 = pygame.sndarray.make_sound(Fs4arr)

    # add vibrato
    violarr = np.round((createSound(sampleRate, 349.23, bits, duration) / 2 + createSound(sampleRate, 10, bits, duration) / 10)).astype(dtype=np.int16)
    viola = pygame.sndarray.make_sound(violarr)
    viola.play(loops=2)
    pygame.time.delay(1000)
    viola.stop()

    plt.plot(violarr)
    plt.ylabel('amplitude')
    plt.xlabel('samples')
    plt.show()
    exit()
    # play sounds play music of here
    for i in range(2):
        G4.play(loops=2)
        pygame.time.delay(1000)
        G4.stop()

        As4.play(loops=1)
        pygame.time.delay(400)
        As4.stop()

        C5.play(loops=1)
        pygame.time.delay(500)
        C5.stop()

        G4.play(loops=2)
        pygame.time.delay(1000)
        G4.stop()

        F4.play(loops=1)
        pygame.time.delay(400)
        F4.stop()

        Fs4.play(loops=1)
        pygame.time.delay(500)
        Fs4.stop()

    final = G4arr[:, 0].tolist() + G4arr[:, 0].tolist() + As4arr[:, 0].tolist() + C5arr[:, 0].tolist()

    plt.plot(final)
    plt.ylabel('amplitude')
    plt.xlabel('samples')
    plt.show()
