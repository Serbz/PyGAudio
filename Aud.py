import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import numpy as np
import time
import math
import datetime, wave, struct, wavio
#import encoding as PCMEncoding
#import math
#from math import *
#import statistics
#from statistics import mean

#use this, maybe difference samples from each wav and compile to new wav

from enum import IntEnum

class PCMEncoding(IntEnum):
    UNSIGNED_8 = 1
    SIGNED_16 = 2
    SIGNED_24 = 3
    SIGNED_32 = 4

wdir = r"D:\\GP\\PyGAud - PyTIR - TTS\\"
now = datetime.datetime.now()
t = now.strftime("%d%m%y_%H%M%S")
inputFile = open(fr"{wdir}\aud.py", "r")
exportFile = open(fr"{wdir}\bak\aud{t}.py", "w")
for line in inputFile:
    new_line = line.replace('\t', '    ')
    exportFile.write(new_line)
inputFile.close()
exportFile.close()

db_accuracy_val = 50

sample_rate = None
samples = None
samples4 = []
audiofile = fr"{wdir}\untitled.wav"
diffaudiofile = fr"{wdir}\untitled2.wav"
sample_rate1, samples1 = wavfile.read(audiofile)
sample_rate2, samples2 = wavfile.read(diffaudiofile)
print(fr"samples1", samples1)
#print(fr"samples2", samples2)
print(fr"sample_rate1", sample_rate1)
#print(fr"sample_rate2", sample_rate2)
sampwidth = wave.open(diffaudiofile).getsampwidth()
nframes1 = wave.open(diffaudiofile).getnframes()
frames1 = wave.open(diffaudiofile).readframes(nframes1)
#nframes2 = wave.open(diffaudiofile).getnframes()
#frames2 = wave.open(diffaudiofile).readframes(nframes2)
print(sampwidth)
print(sample_rate1)
print(nframes1)
try:
    triplets = np.frombuffer(frames1, "u1").reshape(-1, 3)
    padded = np.pad(triplets, ((0, 0), (0, 1)), mode="constant")
    samplesf = padded.flatten().view("<i4")
except:
    triplets = None
    padded = None
    samplesf = None
    pass
#triplets = np.frombuffer(frames2, "u1").reshape(-1, 3)
#padded = np.pad(triplets, ((0, 0), (0, 1)), mode="constant")
#samplesf2 = padded.flatten().view("<i4")
#print(fr"samplesf", samplesf)
#print(fr"samplesf2", samplesf2)
#print(fr"samples1", samples1)
#print(fr"samples2", samples2)
print(fr"samples1", np.asarray(samples1).shape)
#print(fr"samples2", np.asarray(samples2).shape)
print(fr"samplesf", np.asarray(samplesf).shape)
#print(fr"samplesf2", np.asarray(samplesf2).shape)
#samplesf[samples > self.max] += 2 * self.min

#16,777,216
#print(encoding)


try:
    os.remove(fr"{wdir}\samplesf.log")
except:
    pass
try:
    os.remove(fr"{wdir}\samples1.log")
except:
    pass
#try:
#    with open(fr"{wdir}\samplesf.log","w") as f:
#        for each in samplesf:
#            f.write(str(each)+"\n")
#    f.close()
#except:
#    pass
new_samples = []
new_samples2 = []
new_samples3 = []
new_samples4 = []
va = 0
vavg = 0
counter = 1
for each in samples1:
    counter += 1
    v = each
    v2 =(each/counter)
    #v4 =(counter*each)
   # v3 = np.int32(((np.int32(sample_rate1*each))/16777216)*counter)
    #v3 = each/counter
    va += v
    vavg = va/counter
    v5vavg = 16777216*(each/vavg)
    #print("#############")
    #print(v)
    #print(v2)
    #print(v3)
    #print(v4)
    #print("#############")
    new_samples.append(v2)
    #new_samples2.append(v3)
    #new_samples3.append(v4)
    #new_samples4.append(v5vavg)
counter = -1
print(len(samples1),len(samples2))
print(np.asarray(samples1).shape,np.asarray(samples2).shape)
for each in samples2:
    counter += 1
    v = (each*8) - samples1[counter]
    new_samples3.append(v)
counter = -1
for each in samples2:
    counter += 1
    v = samples1[counter] - (each*8)
    new_samples2.append(v)
counter = -1
for each in new_samples2:
    counter += 1
    new_samples4.append(each)
    new_samples4.append(new_samples3[counter])
    
#wavio.write(fr"{wdir}\sound3.wav", new_samples4, sample_rate1, sampwidth=sampwidth)
print("first done")
wavio.write(fr"{wdir}\difference_1.wav", new_samples2, sample_rate1, sampwidth=sampwidth)
wavio.write(fr"{wdir}\Long1.wav", new_samples4, sample_rate1, sampwidth=sampwidth)
print("seond dun")
wavio.write(fr"{wdir}\difference_2.wav", new_samples3, sample_rate1, sampwidth=sampwidth)
#wavio.write(fr"{wdir}\sound2.wav", new_samples3, sample_rate1, sampwidth=sampwidth)
