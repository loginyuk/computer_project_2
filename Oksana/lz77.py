class LZ77:
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size

    def find_longest_match(self, text, current_pos, max_length):
        buffer_start = max(0, current_pos - self.buffer_size)
        buffer = text[buffer_start:current_pos]
        best_offset, best_length = 0, 0
        for offset in range(1, min(current_pos, self.buffer_size) + 1):
            pattern = text[current_pos:current_pos + offset]
            match_pos = buffer.rfind(pattern)
            if match_pos == -1:
                break
            match_length = offset
            while (current_pos + match_length < len(text) and
                   match_length < max_length and
                   text[buffer_start + match_pos + match_length]\
                     == text[current_pos + match_length]):
                match_length += 1
            if match_length > best_length:
                best_offset, best_length = current_pos - buffer_start - match_pos, match_length
                if best_length == max_length:
                    break
        if current_pos + best_length >= len(text):
            best_length = len(text) - current_pos
        return best_offset, best_length

    def encode(self, text):
        result, pos = [], 0
        while pos < len(text):
            offset, length = self.find_longest_match(text, pos, self.buffer_size)
            next_char = text[pos + length] if pos + length < len(text) else ''
            result.append((offset, length, next_char))
            pos += length + 1
        return result

    def decode(self, encoded) -> str:
        """
        This methode decode encoding into string.
        """
        decoded = ''
        for item in encoded:
            if item[1] != 0:
                start_index = len(decoded) - item[0]
                for i in range(item[1]):
                    decoded += decoded[start_index+i]
                decoded += item[2]
            else:
                decoded += item[2]
        return decoded
