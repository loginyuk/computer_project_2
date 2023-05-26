"""
Module that handles
the where to distribute the file
compressing and decompressing of the file
using to the required algorithm
"""

from Algorithms.lzw import LZW
from image_data import work_with_image
from video_data import work_with_video
from audio_data import work_with_audio

def compress(path: str, algorithm: str):
    """
    Args:
        - path: str, the path/name of file with extention
        - algorithm: str, name of the required algorithm
    Return:
        - file_path: str, decompressed file path
    """
    file_type = path.split('.')[-1]

    # TEXT
    if file_type in ['txt']:
        string = ''
        #Read data from a file
        with open(path, encoding="UTF-8") as file:
            data = file.read()
            data = '/'.join(data.split('\n'))
        algorithm = globals()[algorithm]
        decompressed, statistics = algorithm(data)
        assert decompressed == data
        with open(path, 'w', encoding='UTF-8') as file:
            decompressed = decompressed.split('/')
            for element in decompressed:
                string += element + '\n'
            file.write(string)
    # PICTURE
    elif file_type in ['jpg', 'png', 'jpeg']:
        work_with_image(path, algorithm)
    # VIDEO
    elif file_type == 'mp4':
        work_with_video(path, algorithm)
    # AUDIO
    elif file_type in ['mp3', 'wav', 'flac']:
        work_with_audio(path, algorithm)
    else:
        print('File type not supported')
        return None
    return path
