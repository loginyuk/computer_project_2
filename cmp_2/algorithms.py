"""
module that handles the compression of a str
using the required algo, determines the effectiveness and time
"""
import time
from Algorithms.lzw import LZW
from Algorithms.lz77 import LZ77
from Algorithms.huffman import huffman_statistic
from Algorithms.deflate import Deflate
from Algorithms.LZSS import LZSS
from Algorithms.compression_statistics import get_compression_statistics

def lzw_handler(data):
    """
    LZW algorithm handler
    """
    lzw = LZW()
    compressed_text = lzw.encode(data)
    decompressed_data = lzw.decode(compressed_text)
    assert decompressed_data == data
    return decompressed_data, (lzw.compression_ratio, lzw.compression_time, lzw.decompression_time)

def lz77_handler(data):
    """
    LZ77 algorithm handler
    """
    lz77 = LZ77()

    # Стиснення
    start_time = time.time()
    compressed_data = lz77.encode(data)
    compression_time = time.time() - start_time

    # Розтиснення
    start_time = time.time()
    decompressed_data = lz77.decode(compressed_data)
    decompression_time = time.time() - start_time

    # Відсоток стиснення
    compression_ratio = (1 - (len(compressed_data) / len(data))) * 100
    assert decompressed_data == data
    return decompressed_data, (compression_ratio, compression_time, decompression_time)

def huffman_handler(data):
    """
    Huffman algorithm handler
    """
    statistics, decompressed_data = huffman_statistic(data)
    assert decompressed_data == data
    return decompressed_data, statistics

def deflate_handler(data):
    """
    Deflate algorithm handler
    """
    statistics = []
    statistics, decompressed = get_compression_statistics(Deflate(), data)
    assert decompressed == data
    return decompressed, statistics

def lzss_handler(data):
    """
    LZSS algorithm handler
    """
    statistics, decompressed_data = get_compression_statistics(LZSS(), data)
    assert decompressed_data == data
    return decompressed_data, statistics

def work_with_algo(algorithm, data):
    algorithm = algorithm.lower() + '_handler'
    algorithm = globals()[algorithm]
    decompressed, statistics = algorithm(data)
    return decompressed, statistics
