import pydub 
import numpy as np

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

sr, x = read("computer_project_2/Yura/audio.mp3")
# print(x)


import wave
import numpy as np

# Open the WAV file
with wave.open('computer_project_2/Yura/audio.wav', 'rb') as wav_file:
    # Get audio parameters
    sample_width = wav_file.getsampwidth()
    sample_rate = wav_file.getframerate()
    num_channels = wav_file.getnchannels()
    num_frames = wav_file.getnframes()

    # Read audio samples
    audio_data = wav_file.readframes(num_frames)

    # Convert the raw audio data to a numpy array of samples
    audio_samples = np.frombuffer(audio_data, dtype=np.int16)

# Print the first 10 audio samples
print(audio_samples)

from scipy.io import wavfile
wavfile.write('computer_project_2/Yura/audio.wav', sample_rate, audio_samples)
