"""LZ77 algorithm"""
class LZ77:
    """class for LZ77 algorithm"""
    def __init__(self) -> None:
        """
        Init a lz77 class with a buffer length.
        Default set to 255.
        """
        self.buffer_length = 255

    def find_substring(self, buffer, data):
        """
        Find the longest common substring in the buffer.
        """
        length = 0
        offset = 0
        while length < len(data):
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



    def encode(self, data):
        """
        Compress the data.
        """
        ans = []
        buffer = ""
        while data:
            length, code = self.find_substring(buffer, data)
            buffer += data[:length + 1]
            if len(buffer) > self.buffer_length:
                buffer = buffer[len(buffer) - self.buffer_length:]
            data = data[length + 1:]
            ans.append(code)
        data = ans
        return ans

    def decode(self, data):
        """
        Decompress the data.
        """
        buffer = ""
        ans = ""
        for (offset, length, next) in data:
            if next is None:
                ans += buffer[len(buffer) - offset:len(buffer) - offset + length]
                break
            added = buffer[len(buffer) - offset:len(buffer) - offset + length] + next
            ans += added
            buffer += added
            if len(buffer) > self.buffer_length:
                buffer = buffer[len(buffer) - self.buffer_length:]
        return ans

# lz = LZ77()
# with open('delete', 'r') as file:
#     a = file.read()
# encoded = lz.encode(a)
# decoded = lz.decode(encoded)
# print(decoded == a)
