import numpy as np

import pydub 

from scipy.io import wavfile

import soundfile as sf


# MP3

def read(f, normalized=False):
    """MP3 to numpy array"""
    a = pydub.AudioSegment.from_mp3(f)
    y = np.array(a.get_array_of_samples())
    if a.channels == 2:
        y = y.reshape((-1, 2))
    if normalized:
        return a.frame_rate, np.float32(y) / 2**15
    else:
        return a.frame_rate, y

def write(f, sr, x, normalized=False):
    """numpy array to MP3"""
    channels = 2 if (x.ndim == 2 and x.shape[1] == 2) else 1
    if normalized:  # normalized array - each item should be a float in [-1, 1)
        y = np.int16(x * 2 ** 15)
    else:
        y = np.int16(x)
    song = pydub.AudioSegment(y.tobytes(), frame_rate=sr, sample_width=2, channels=channels)
    song.export(f, format="mp3", bitrate="320k")


# читання mp3 файлу
rate, data_mp3 = read("Yura/audio.mp3")

# стрінга з числами розділена крапкою
string = '.'.join(data_mp3.flatten().astype(str))

# перетворення в numpy array
array = np.array([int(num) for num in string.split('.')]).reshape((len(data_mp3), 2)).astype(np.int16)

# запис в wav файл
write('Yura/new.mp3',rate,array)





# Wav

# читання wav файлу
rate, data_wav = wavfile.read('Yura/audio.wav')

# стрінга з числами розділена крапкою
string = '.'.join(data_wav.flatten().astype(str))

# перетворення в numpy array
array = np.array([int(num) for num in string.split('.')]).reshape((len(data_wav), 2)).astype(np.int16)

wavfile.write('Yura/new.wav',rate,array)








# Flac
audio_path = "Yura/sample3.flac"
audio_data, sample_rate = sf.read(audio_path)

flac = '/'.join(audio_data.flatten().astype(str))

array = np.array([float(num) for num in flac.split('/')]).reshape((len(audio_data), 2)).astype(np.float32)

sf.write('Yura/new.flac',array,sample_rate)
