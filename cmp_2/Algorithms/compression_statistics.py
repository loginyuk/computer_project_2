"""test algo-s"""
import time
from LZSS import LZSS
from lzw import LZW
from lz77 import LZ77
from lzcompres import LZCompression

def get_compression_statistics(algorithm_compress, original_data):
    """
    Розраховує відсоток стиснення тексту, час стиснення та розтиснення.

    Параметри:
    - algorithm_compress: Алгоритм, яким буде стиснутий.
    - data (str): дані для стиску.

    Повертає:
    відсоток стиснення, час стиснення та час розтиснення.
    """
    start_compress_time = time.time()
    compressed_data = algorithm_compress.encode(original_data)
    end_compress_time = time.time()
    compress_time = end_compress_time - start_compress_time
    print(compressed_data)
    start_decompress_time = time.time()
    decompressed_data = algorithm_compress.decode(compressed_data)
    end_decompress_time = time.time()
    decompress_time = end_decompress_time - start_decompress_time

    original_size = len(original_data)
    compressed_size = len(compressed_data) * 2  # Розмір стиснутих даних, враховуючи довжину і зміщення


    compression_ratio = (compressed_size / original_size) * 100

    return compression_ratio, compress_time, decompress_time, decompressed_data



# with open('text.txt', 'r', encoding="utf-8") as file:
#     data = file.read()

# # Приклад використання
# data = "aaasdasd asdasdasdasd asd"
# compression_ratio, compress_time, decompress_time, decompressed_data = get_compression_statistics(LZ77(), data)

# print("Compression ratio:\t{:.2f}%".format(compression_ratio))
# print("Compression time:\t{:.6f} seconds".format(compress_time))
# print("Decompression time:\t{:.6f} seconds".format(decompress_time))
