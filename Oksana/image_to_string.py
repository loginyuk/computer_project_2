from PIL import Image
import base64


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
    return result_list


image_path = 'flower.jpg'
image_string = image_to_string(image_path)

encode_string = compress(image_string)

print(encode_string)
print('Original image string length:', len(image_string))

