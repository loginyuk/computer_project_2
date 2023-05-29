"""
module that handles the compression of a str
using the required algo, determines the effectiveness and time
"""

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
    #compression ratio, compress time, decompress time
    statistics, decompressed_data = get_compression_statistics(LZW(), data)
    assert decompressed_data == data
    return decompressed_data, statistics

def lz77_handler(data):
    """
    LZ77 algorithm handler
    """
    statistics, decompressed_data = get_compression_statistics(LZ77(), data)
    assert decompressed_data == data
    return decompressed_data, statistics

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
