class LZW:
    def __init__(self, string):
        s = {x for x in string}
        sorted_list = sorted(s)
        self.dictionary_size = len(sorted_list)
        self.dictionary = {sorted_list[i]: i for i in range(self.dictionary_size)}
        self.string = string

    def encode(self):
        result_list = []
        sequence = ""
        for character in self.string:
            new_sequence = sequence + character
            if new_sequence in self.dictionary:
                sequence = new_sequence
            else:
                result_list.append(self.dictionary[sequence])
                self.dictionary[new_sequence] = self.dictionary_size
                self.dictionary_size += 1
                sequence = character
        if sequence:
            result_list.append(self.dictionary[sequence])
        res = ""
        return result_list

    def decode(self, code):
        reverse_dict = {v: k for k, v in self.dictionary.items()}
        message = ""
        i = 0
        while i < len(code):
            if code[i] in reverse_dict:
                message += reverse_dict[code[i]]
                i += 1
            else:
                raise ValueError("Invalid code")
        return message
