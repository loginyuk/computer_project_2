"""Huffman algo"""

class HuffmanVertex:
    """
    Class to represent a Vertex in the Huffman tree.
    """
    def __init__(self, character=None, frequency=0, top=None, bottom=None):
        self.character = character
        self.frequency = frequency
        self.top = top
        self.bottom = bottom
        self.code = ''

    def __lt__(self, other):
        "Sorting by freq"
        return self.frequency < other.frequency

class HuffmanTree:
    """
    Class to represent the Huffman tree.
    """
    def __init__(self, data):
        self.root = None
        self.encode_text = {}
        self.decode_text = {}
        self.build_tree(data)
        self.build_textes(self.root)

    def build_tree(self, data):
        """
        Build the Huffman tree from the given data.
        """
        frequency = {}
        for character in data:
            # розраховує вирогідність кожного символу в тексті
            frequency[character] = frequency.get(character, 0) + 1
        vertexes = [HuffmanVertex(character=character, frequency=freq)\
 for character, freq in frequency.items()]
        while len(vertexes) > 1:
            vertexes = sorted(vertexes)
            top = vertexes.pop(0)
            bottom = vertexes.pop(0)
            # робить суму останніх двох елементів
            parent_vert = HuffmanVertex(frequency=top.frequency + bottom.frequency,\
 top=top, bottom=bottom)
            vertexes.append(parent_vert)
        self.root = vertexes[0]

    def build_textes(self, vertex, code=''):
        """
        Build the encoding and decoding tables from the Huffman tree.
        """
        if vertex is None:
            return
        if vertex.character is not None:
            vertex.code = code
            self.encode_text[vertex.character] = code
            self.decode_text[code] = vertex.character
        self.build_textes(vertex.top, code + '0')
        self.build_textes(vertex.bottom, code + '1')

    def encode(self, data):
        """
        Encode the given data using the Huffman tree.
        """
        encoded_data = ''
        for character in data:
            encoded_data += self.encode_text[character]
        return encoded_data

    def decode(self, data):
        """
        Decode the given data using the Huffman tree.
        """
        decoded_data = ''
        current_code = ''
        for bit in data:
            current_code += bit
            if current_code in self.decode_text:
                decoded_data += self.decode_text[current_code]
                current_code = ''
        return decoded_data

# data = 'aabbbcdddddeeeeee'
# huffman_tree = HuffmanTree(data)
# encoded_data = huffman_tree.encode(data)
# print(encoded_data)
# decoded_data = huffman_tree.decode(encoded_data)
# print(decoded_data)
