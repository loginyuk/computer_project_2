from image_to_string import work_with_image
# from text_to_string import work_with_text
from video_data import work_with_video
from audio_data import work_with_audio


def compress(path, algorithm):
    #function that returns path to the compressed file

    file_type = path.split('.')[-1]
    if file_type == 'txt':
        ...
    elif file_type in ['jpg', 'png', 'jpeg']:
        work_with_image(path, algorithm)
    elif file_type == 'mp4':
        work_with_video(path, algorithm)
    elif file_type in ['mp3', 'wav', 'flac']:
        work_with_audio(path, algorithm)
    else:
        print('File type not supported')
        return None


    return path