"""
module that handles the compression of a str
using the required algo, determines the effectiveness and time
"""

from Algorithms.lzw import LZW
from Algorithms.lz77 import LZ77
from Algorithms.huffman import HuffmanTree
from Algorithms.deflate import Deflate

def LZW(data):
    """o"""
    statistics = []
    compressed = LZW(data).encode()
    decompressed = LZW(compressed).decode()
    assert decompressed == data
    return decompressed, statistics

def LZ77(data):
    """o"""
    statistics = []
    lz = LZ77(data)
    compressed = lz.compress()
    decompressed = lz.decompress()
    assert decompressed == data
    return decompressed, statistics

def Huffman(data):
    """o"""
    statistics = []
    huffman = HuffmanTree(data)
    compressed = huffman_tree.encode(data)
    decompressed = huffman_tree.decode(compressed)
    assert decompressed == data
    return decompressed, statistics

def Deflate(data):
    """o"""
    ...

def Fifth_algorithm(data):
    """o"""
    ...

