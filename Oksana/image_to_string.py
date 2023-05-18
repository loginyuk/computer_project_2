import base64
import io
import cv2
from PIL import Image
import numpy as np


def image_to_string(image_path):
    with Image.open(image_path) as img:
        # Convert image to byte array
        img_to_byte = img.tobytes()

        # Encode byte array as base64 string
        img_base64 = base64.b64encode(img_to_byte).decode('utf-8')

        return img_base64


def compress(string):
    s = {x for x in string}
    sorted_list = sorted(s)
    dictionary_size = len(sorted_list)
    dictionary = {sorted_list[i]: i for i in range(dictionary_size)}
    string = string
    result_list = []
    sequence = ""
    for character in string:
        new_sequence = sequence + character
        if new_sequence in dictionary:
            sequence = new_sequence
        else:
            result_list.append(dictionary[sequence])
            dictionary[new_sequence] = dictionary_size
            dictionary_size += 1
            sequence = character
    if sequence:
        result_list.append(dictionary[sequence])
    return result_list, dictionary


def decompress(code, dictionary):
    reverse_dict = {v: k for k, v in dictionary.items()}
    message = ""
    i = 0
    while i < len(code):
        if code[i] in reverse_dict:
            message += reverse_dict[code[i]]
            i += 1
        else:
            raise ValueError("Invalid code")
    return message


def string_to_image(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    img = Image.frombytes("RGB", (640, 480), imgdata)
    opencv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    return opencv_img


image_path = 'nature.jpg'
image_string = image_to_string(image_path)
# print(image_string)
#
compressed = compress(image_string)
decompressed = decompress(compressed[0], compressed[1])

# # print()
#
# print(decompressed)
# # print(decompressed == image_string)
compresed_string = ''
for i in compressed[0]:
    compresed_string += str(i)
# # print(compresed_string)

string_image = string_to_image(decompressed)

data = Image.fromarray(string_image)

# saving the final output
# as a PNG file
data.save('gfg_dummy_pic.png')

# print('Original image string length:', len(image_string))
# print('Compressed image string length:', len(compressed[0]))
# print('Decompressed image string length:', len(decompressed))
