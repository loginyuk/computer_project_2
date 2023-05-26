"""LZ77 algorithm"""
class LZ77:
    """class for LZ77 algorithm"""
    def __init__(self, data) -> None:
        """
        Init a lz77 class with a buffer length.
        Default set to 255.
        """
        self.buffer_length = 255
        self.data = data

    def find_substring(self, buffer, data):
        """
        Find the longest common substring in the buffer.
        """
        length = 0
        offset = 0
        while True:
            it = buffer.find(data[:length + 1])
            if it != -1:
                offset = len(buffer[it:])
                length += 1
                if data[:length] == data[:length + 1]:
                    return (length, (offset, length, None))
                continue
            break
        next = data[length]
        return (length, (offset, length, next))

    def compress(self):
        """
        Compress the data.
        """
        ans = []
        buffer = ""
        while self.data:
            length, code = self.find_substring(buffer, self.data)
            buffer += self.data[:length + 1]
            if len(buffer) > self.buffer_length:
                buffer = buffer[len(buffer) - self.buffer_length:]
            self.data = self.data[length + 1:]
            ans.append(code)
        self.data = ans
        return ans

    def decompress(self):
        """
        Decompress the data.
        """
        buffer = ""
        ans = ""
        for (offset, length, next) in self.data:
            if next == None:
                ans += buffer[len(buffer) - offset:len(buffer) - offset + length]
                break
            added = buffer[len(buffer) - offset:len(buffer) - offset + length] + next
            ans += added
            buffer += added
            if len(buffer) > self.buffer_length:
                buffer = buffer[len(buffer) - self.buffer_length:]
        self.data = ans
        return ans


    def calculate_compression(self):
        """
        Calculate compression.
        """
        tuples = int(self.data.count('|') / 2)
        bits = (8 + 2 * (len(bin(self.buffer_length).split('b')[1]))) * tuples
        return int(bits / 8)


lz = LZ77(255, 'adghjgvgvm')
encoded = lz.compress()
print(encoded)
decoded = lz.decompress()
print(decoded)
