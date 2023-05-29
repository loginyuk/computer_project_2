"""Deflate algorithm"""
from Algorithms.lz77 import LZ77
from Algorithms.huffman1 import HuffmanTree

class Deflate:
    """Class for Deflate algorithm"""
    def __init__(self):
        self.lz77 = LZ77()
        self.huf = None

    def encode(self, data):
        """
        Encode the data.
        """
        compressed_data = self.lz77.encode(data)
        self.huf = HuffmanTree(compressed_data)
        encoded_data = self.huf.encode(compressed_data)
        return encoded_data

    def decode(self, encoded_data):
        """
        Decode the data.
        """
        decoded_data = self.huf.decode(encoded_data)
        self.lz77.data = decoded_data
        decompressed_data = self.lz77.decode(decoded_data)
        return decompressed_data
