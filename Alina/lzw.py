from io import StringIO

class Code:
    def __init__(self, uncompressed) -> None:
        self.uncompressed = uncompressed

    def encode(self):
        """Compress a string to a list of output symbols."""

        dict_size = 256
        dictionary = dict((chr(element), element) for element in range(dict_size))


        text = ""
        result = []
        for elem in self.uncompressed:
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
        return result


    def decode(self):
        """Decompress a list of output ks to a string."""

        dict_size = 256
        dictionary = dict((element, chr(element)) for element in range(dict_size))

        result = StringIO()
        text = chr(self.uncompressed.pop(0))
        result.write(text)
        for lem in self.uncompressed:
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
        return result.getvalue()

compress = Code('TOBEORNOTTOBEORTOBEORNOT').encode()
print (compress)
decompress = Code(compress).decode()
print(decompress)