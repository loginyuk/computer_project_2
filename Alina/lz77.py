class lz77:
    def __init__(self, buffer_length=255) -> None:
        """
        Init a lz77 class with a buffer length.
        Default set to 255.
        """
        self.buffer_length = buffer_length

    def read(self, file_path):
        """
        Read data from a file.
        """
        with open(file_path, encoding="UTF-8") as file:
            self.data = file.read()
    
    def write(self, file_path):
        """
        Write data into a file.
        """
        with open(file_path,'w', encoding="UTF-8") as file:
            file.write(str(self.data))

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

    def decompress(self):
        """
        Decompress the data.
        """
        buffer = ""
        ans = ""
        for (offset, length, next) in self.data:
            if next == None:
                ans +=  buffer[len(buffer) - offset:len(buffer) - offset + length]
                break
            added = buffer[len(buffer) - offset:len(buffer) - offset + length] + next
            ans += added
            buffer += added
            if len(buffer) > self.buffer_length:
                buffer = buffer[len(buffer) - self.buffer_length:]
        self.data = ans

        

    def encode(self, file_path):
        """
        Encode data from a file and write into the new file.
        """
        self.read(file_path)
        self.compress()
        self.write(f"{file_path.split('.')[0]}_compressed.txt")

    def decode(self, file_path):
        """
        Decode a code from a file.
        """
        self.decompress()
        self.write(f"{file_path.split('.')[0]}_decompressed.txt")

    def calculate_compression(self):
        """
        Calculate compression.
        """
        tuples = int(self.data.count('|')/2)
        bits = (8 + 2 * (len(bin(self.buffer_length).split('b')[1]))) * tuples
        return int(bits / 8)



lz = lz77(255)
lz.encode('introductiontoalgoritms.txt')
lz.decode('introductiontoalgoritms_compressed.txt')
with open('introductiontoalgoritms.txt', encoding="UTF-8") as file:
            orig = file.read()
with open('introductiontoalgoritms_compressed_decompressed.txt', encoding="UTF-8") as file:
            new = file.read()

assert orig == new