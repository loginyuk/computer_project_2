"""test algo-s"""
import time

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
    start_decompress_time = time.time()
    decompressed_data = algorithm_compress.decode(compressed_data)
    end_decompress_time = time.time()
    decompress_time = end_decompress_time - start_decompress_time

    original_size = len(original_data)
    # Розмір стиснутих даних, враховуючи довжину і зміщення
    compressed_size = len(compressed_data) * 2
    compression_ratio = (compressed_size / original_size) * 100

    return [compression_ratio, compress_time, decompress_time], decompressed_data
