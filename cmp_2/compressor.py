"""
Module that handles
the where to distribute the file
compressing and decompressing of the file
using to the required algorithm
"""

from Algorithms.lzw import LZW


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
    if extention in ['txt']:
        string = ''
        #Read data from a file
        with open(path, encoding="UTF-8") as file:
            data = file.read()
            data = '/'.join(data.split('\n'))
        decompressed = find_algo(algorithm, data)
        assert decompressed == data
        with open('decompressed.txt', 'w', encoding='UTF-8') as file:
            decompressed = decompressed.split('/')
            for element in decompressed:
                string += element + '\n'
            file.write(string)
            return 'decompressed.txt'

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


def find_algo(name: str, data: str) -> str:
    """find and use the required algo"""
    if name == 'Huffman':
        pass
    if name == 'LZW':
        lzw = LZW(data)
        compressed = lzw.encode()
        decompressed = LZW(compressed).decode()
        assert data == decompressed
        return decompressed
    if name == 'LZ77':
        pass
    if name == 'Deflate':
        pass
    if name == 'Fifth algorithm':
        pass

text = compress("/Users/alina.babenko/Desktop/Дискретна мат/2_sem/computer_project_2/Alina/bible.txt", 'LZW')
print(text)
# current_directory = Path.cwd()
# print(current_directory)