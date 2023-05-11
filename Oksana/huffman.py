class Node:
    def __init__(self, character=None, frequency=0, left=None, right=None):
        self.character = character
        self.frequency = frequency
        self.left = left
        self.right = right


class HuffmanCode:
    def __init__(self):
        self.frequency_dict = {}
        self.code_dict = {}

    def build_freq_dict(self, data):
        for character in data:
            if character in self.frequency_dict:
                self.frequency_dict[character] += 1
            else:
                self.frequency_dict[character] = 1

    def build_tree(self):
        nodes = []
        for character, frequency in self.frequency_dict.items():
            nodes.append(Node(character=character, frequency=frequency))

        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.frequency)
            left = nodes.pop(0)
            right = nodes.pop(0)
            parent = Node(frequency=left.frequency + right.frequency, left=left, right=right)
            nodes.append(parent)

        return nodes[0]

    def build_code_dict(self, node, code=''):
        if not node.left and not node.right:
            self.code_dict[node.character] = code
        else:
            self.build_code_dict(node.left, code + '0')
            self.build_code_dict(node.right, code + '1')

    def encode(self, data):
        self.build_freq_dict(data)
        tree = self.build_tree()
        self.build_code_dict(tree)
        encoded_data = ''.join([self.code_dict[character] for character in data])
        return encoded_data

    def decode(self, encoded_data):
        decoded_text = ''
        current = tree = self.build_tree()
        for bit in encoded_data:
            current = current.left if bit == '0' else current.right
            if not current.left and not current.right:
                decoded_text += current.character
                current = tree

        return decoded_text
