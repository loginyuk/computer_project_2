import base64
import io
from PIL import Image
import numpy as np
from algorithms import work_with_algo

def image_to_string(image_path_: str) -> tuple:
    """
    Convert an image to a base64-encoded string and retrieve its size.

    Parameters:
        image_path_ (str): The path to the image file.

    Returns:
        tuple: A tuple containing the base64-encoded image string and its size.
    """
    with Image.open(image_path_) as img:
        # Encode image as base64 string
        byte_stream = io.BytesIO()
        # Save using the original image format
        img.save(byte_stream, format=img.format)
        byte_stream.seek(0)
        img_base64 = base64.b64encode(byte_stream.read()).decode('utf-8')
        return img_base64, img.size, img.format


# def compress(string):
#     s = {x for x in string}
#     sorted_list = sorted(s)
#     dictionary_size = len(sorted_list)
#     dictionary = {sorted_list[i]: i for i in range(dictionary_size)}
#     result_list = []
#     sequence = ""
#     for character in string:
#         new_sequence = sequence + character
#         if new_sequence in dictionary:
#             sequence = new_sequence
#         else:
#             result_list.append(dictionary[sequence])
#             dictionary[new_sequence] = dictionary_size
#             dictionary_size += 1
#             sequence = character
#     if sequence:
#         result_list.append(dictionary[sequence])
#     return result_list, dictionary


# def decompress(code, dictionary):
#     reverse_dict = {v: k for k, v in dictionary.items()}
#     message = ""
#     i = 0
#     while i < len(code):
#         if code[i] in reverse_dict:
#             message += reverse_dict[code[i]]
#             i += 1
#         else:
#             raise ValueError("Invalid code")
#     return message


def string_to_image(base64_string: str, size: tuple):
    """
    Convert a base64-encoded string back into an image.

    Parameters:
        base64_string (str): The base64-encoded image string.
        size (tuple): The desired size of the output image.

    Returns:
        tuple: A tuple containing the NumPy array representation of the image and its format.
    """
    imgdata = base64.b64decode(str(base64_string))
    img = Image.open(io.BytesIO(imgdata))
    img = img.convert("RGB")  # Convert to RGB color space
    img = img.resize(size)    # Resize the image if necessary
    return np.array(img)


def work_with_image(image_path, algorithm):
    image_string, resolution, original_format = image_to_string(image_path)

    decompressed, statistics = work_with_algo(algorithm, image_string)



    string_image = string_to_image(decompressed, resolution)
    data = Image.fromarray(string_image)
    output_path = image_path.split('.')[1]

    # Save the image with the correct format
    print('Saving as...', output_path)
    data.save(output_path, format=original_format)

    return statistics



# if __name__ == '__main__':
#     # image_path = 'Oksana/ex1.jpeg'
#     # image_path = 'Oksana/ex2.tiff'
#     image_path = 'Oksana/ex3.png'
#     image_string, resolution, original_format = image_to_string(image_path)

#     compressed = compress(image_string)
#     decompressed = decompress(compressed[0], compressed[1])

#     string_image = string_to_image(decompressed, resolution)
#     data = Image.fromarray(string_image)
#     output_path = 'Oksana/final.' + original_format.lower()

#     # Save the image with the correct format
#     print('Saving as...', output_path)
#     data.save(output_path, format=original_format)

