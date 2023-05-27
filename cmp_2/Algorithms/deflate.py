"""Deflate algorithm"""
from lz77 import LZ77
from huffman import HuffmanTree

class Deflate:
    """Class for Deflate algorithm"""
    def __init__(self, data):
        self.data = data
        self.lz77 = LZ77(data)
        self.huf = HuffmanTree(data)

    def encode(self):
        """
        Encode the data.
        """
        compressed_data = self.lz77.compress()
        encoded_data = self.huf.encode(compressed_data)
        return encoded_data

    def decode(self, encoded_data):
        """
        Decode the data.
        """
        decoded_data = self.huf.decode(encoded_data)
        self.lz77.data = decoded_data
        decompressed_data = self.lz77.decompress()
        return decompressed_data
