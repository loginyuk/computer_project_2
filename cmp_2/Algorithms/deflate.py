"""Deflate algorithm"""
from lz77 import LZ77
from huffman import HuffmanTree

class Deflate:
    """class for Deflate algorithm"""
    def __init__(self, data):
        self.data = data
        self.lz = LZ77()
        self.huf = HuffmanTree()

    def read(self, file_path):
        """
        Read data from a file.
        """
        with open(file_path, encoding="UTF-8") as file:
            self.data = file.read()

    def write(self, data, file_path):
        """
        Write data into a file.
        """
        with open(file_path,'w', encoding="UTF-8") as file:
            file.write(data)

    def encode(self, file_path):
        """
        Encode the data.
        """
        self.lz.compress(file_path)
        self.huf.encode(f'{file_path.split(".")[0]}_compressed.txt')
        self.write(self.huf.coded, f'{file_path.split(".")[0]}_compressed_deflated.txt')

    def decode(self, file_path_in, file_path_out):
        """
        Decode the data.
        """
        data = self.read(file_path_in)
        self.huf.decoded = data
        self.huf.decode(file_path_in)
        self.lz.decompressed = self.read(f'{file_path_in.split(".")[0]}_decompressed.txt')
        self.lz.decode(file_path_out)

