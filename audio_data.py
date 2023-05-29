"""handle audio"""
import numpy as np
import pydub
from scipy.io import wavfile
import soundfile as sf

from algorithms import work_with_algo

def audio_string(path):
    """
    Get info from audio file
    """
    sep = '.'
    bits = np.int16
    file_format = path.split('.')[-1]

    if file_format == 'mp3':
        rate, data = read_mp3(path)
    elif file_format == 'wav':
        rate, data = wavfile.read(path)
    elif file_format == 'flac':
        sep = '/'
        bits = np.float32
        data, rate = sf.read(path)
    else:
        print('Wrong format')

    string = sep.join(data.flatten().astype(str))

    return string, rate, len(data), sep, bits, file_format, path



def audio_back(decompressed, rate, lend, sep, bits, file_format, path):
    """
    Back to audio file
    """
    if file_format == 'flac':
        np_array = np.array([float(num) for num in\
                decompressed.split(sep)]).reshape((lend, 2)).astype(bits)
    else:
        np_array = np.array([int(num) for num in\
                decompressed.split(sep)]).reshape((lend, 2)).astype(bits)

    if file_format == 'mp3':
        write_mp3(path,rate,np_array)
    elif file_format == 'wav':
        wavfile.write(path, rate,np_array)
    elif file_format == 'flac':
        sf.write(path, np_array,rate)


def read_mp3(f, normalized=False):
    """MP3 to numpy array"""
    a = pydub.AudioSegment.from_mp3(f)
    y = np.array(a.get_array_of_samples())
    if a.channels == 2:
        y = y.reshape((-1, 2))
    if normalized:
        return a.frame_rate, np.float32(y) / 2**15
    else:
        return a.frame_rate, y

def write_mp3(f, sr, x, normalized=False):
    """numpy array to MP3"""
    channels = 2 if (x.ndim == 2 and x.shape[1] == 2) else 1
    if normalized:  # normalized array - each item should be a float in [-1, 1)
        y = np.int16(x * 2 ** 15)
    else:
        y = np.int16(x)
    song = pydub.AudioSegment(y.tobytes(), frame_rate=sr, sample_width=2, channels=channels)
    song.export(f, format="mp3", bitrate="320k")


def work_with_audio(path, algorithm):
    data_from_audio = audio_string(path)
    decompressed, statistics = work_with_algo(algorithm, data_from_audio[0])
    audio_back(decompressed, data_from_audio[1], data_from_audio[2], \
            data_from_audio[3], data_from_audio[4], data_from_audio[5], data_from_audio[6])

    return statistics
