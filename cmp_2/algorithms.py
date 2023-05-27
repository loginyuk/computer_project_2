"""
module that handles the compression of a str
using the required algo, determines the effectiveness and time
"""

from Algorithms.lzw import LZW
from Algorithms.lz77 import LZ77
from Algorithms.huffman import HuffmanTree
from Algorithms.deflate import Deflate
from Algorithms.LZSS import LZSS

def lzw_handler(data):
    """o"""
    statistics = []
    compressed = LZW(data).encode()
    decompressed = LZW(compressed).decode()
    assert decompressed == data
    return decompressed, statistics

def lz77_handler(data):
    """o"""
    statistics = []
    lz77 = LZ77(data)
    compressed = lz77.compress()
    decompressed = lz77.decompress()
    assert decompressed == data
    return decompressed, statistics

def huffman_handler(data):
    """o"""
    statistics = []
    huffman = HuffmanTree(data)
    compressed = huffman.encode(data)
    decompressed = huffman.decode(compressed)
    assert decompressed == data
    return decompressed, statistics

def deflate_handler(data):
    """o"""
    statistics = []
    deflate = Deflate()
    compressed = deflate.encode(data)
    decompressed = deflate.decode(compressed)
    assert decompressed == data
    return decompressed, statistics

def lzss_handler(data):
    """o"""
    statistics = []
    lzss = LZSS()
    compressed = lzss.compress(data)
    decompressed = lzss.decompress(compressed)
    assert decompressed == data
    return decompressed, statistics

def work_with_algo(algorithm, data):
    algorithm = algorithm.lower() + '_handler'
    algorithm = globals()[algorithm]
    decompressed, statistics = algorithm(data)
    return decompressed, statistics

# if __name__ == '__main__':
    # a = deflate_handler('ewfgawygef')
    # print(a)
