"""LZW algorithm"""
from io import StringIO

class LZW:
    """class for LZW algorithm"""
    def __init__(self):
        self.compression_ratio = None
        self.compression_time = None
        self.decompression_time = None

    def encode(self, uncompressed):
        """Compress a string to a list of output symbols."""
        import time

        dict_size = 256
        dictionary = dict((chr(element), element) for element in range(dict_size))

        text = ""
        result = []
        start_time = time.time()
        for elem in uncompressed:
            res = text + elem
            if res in dictionary:
                text = res
            else:
                result.append(dictionary[text])
                dictionary[res] = dict_size
                dict_size += 1
                text = elem

        if text:
            result.append(dictionary[text])

        end_time = time.time()
        self.compression_time = end_time - start_time
        uncompressed_length = len(uncompressed)
        compressed_length = len(result)
        self.compression_ratio = (1 - (compressed_length / uncompressed_length)) * 100

        return result

    def decode(self, compressed):
        """Decompress a list of output ks to a string."""
        import time

        dict_size = 256
        dictionary = dict((element, chr(element)) for element in range(dict_size))

        result = StringIO()
        text = chr(compressed.pop(0))
        result.write(text)

        start_time = time.time()
        for lem in compressed:
            if lem in dictionary:
                entry = dictionary[lem]
            elif lem == dict_size:
                entry = text + text[0]
            else:
                return ValueError

            result.write(entry)

            dictionary[dict_size] = text + entry[0]
            dict_size += 1
            text = entry

        end_time = time.time()
        self.decompression_time = end_time - start_time

        decoded_text = result.getvalue()

        return decoded_text
