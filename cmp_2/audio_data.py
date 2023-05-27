"""handle audio"""

import numpy as np
import pydub
from scipy.io import wavfile
import soundfile as sf

from algorithms import work_with_algo


def audio_string(path):
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
    np_array = np.array([int(float(num)) for num in decompressed.split(sep)]).reshape((lend, 2)).astype(bits)
    
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

    


    audio_back(decompressed, data_from_audio[1], data_from_audio[2], data_from_audio[3], data_from_audio[4], data_from_audio[5], data_from_audio[6])
    return statistics






# # читання mp3 файлу
# rate, data_mp3 = read("Yura/audio.mp3")

# # стрінга з числами розділена крапкою
# string = '.'.join(data_mp3.flatten().astype(str))

# # перетворення в numpy array
# array = np.array([int(num) for num in string.split('.')]).reshape((len(data_mp3), 2)).astype(np.int16)

# # запис в wav файл
# write('Yura/new.mp3',rate,array)





# # Wav

# # читання wav файлу
# rate, data_wav = wavfile.read('Yura/audio.wav')

# # стрінга з числами розділена крапкою
# string = '.'.join(data_wav.flatten().astype(str))

# # перетворення в numpy array
# array = np.array([int(num) for num in string.split('.')]).reshape((len(data_wav), 2)).astype(np.int16)

# wavfile.write('Yura/new.wav',rate,array)








# # Flac
# audio_path = "Yura/sample3.flac"
# audio_data, sample_rate = sf.read(audio_path)

# flac = '/'.join(audio_data.flatten().astype(str))

# array = np.array([float(num) for num in flac.split('/')]).reshape((len(audio_data), 2)).astype(np.float32)

# sf.write('Yura/new.flac',array,sample_rate)



# if __name__ == "__main__":
#     path = input()
#     format = path.split('.')[-1]
#     if format == 'mp3':
#         ...
#     elif format == 'wav':
#         ...
#     elif format == 'flac':
#         ...
#     else:
#         print('Wrong format')