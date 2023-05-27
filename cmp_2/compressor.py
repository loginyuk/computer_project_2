"""
Module that handles
the where to distribute the file
compressing and decompressing of the file
using to the required algorithm
"""

# from Algorithms.lzw import LZW
from image_data import work_with_image
from video_data import work_with_video
from audio_data import work_with_audio
from txt_data import work_with_txt

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
    if file_type == 'txt':
        statistics = work_with_txt(path, algorithm)
    # PICTURE
    elif file_type in ['jpg', 'png', 'jpeg']:
        statistics = work_with_image(path, algorithm)
    # VIDEO
    elif file_type == 'mp4':
        statistics = work_with_video(path, algorithm)
    # AUDIO
    elif file_type in ['mp3', 'wav', 'flac']:
        statistics = work_with_audio(path, algorithm)
    else:
        print('File type not supported')
        return None, None
    return path, statistics
