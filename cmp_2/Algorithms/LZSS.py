"""LZSS_algo"""

class LZSS:
    """class LZSS"""
    def __init__(self, window_size=10, lookahead_buffer_size=5):
        """
        Ініціалізує об'єкт алгоритму LZSS з заданим розміром вікна і буфера вигляду.

        Параметри:
        - window_size (int): Розмір вікна, в якому шукається відповідна підстрока.
        - lookahead_buffer_size (int): Розмір буфера вигляду, що визначає 
        максимальну довжину відповідної підстроки.

        """
        self.window_size = window_size
        self.lookahead_buffer_size = lookahead_buffer_size

    def compress(self, data):
        """
        Стискає вхідні дані за допомогою алгоритму LZSS.

        Параметри:
        - data (str): Рядок, що містить вхідні дані для стиснення.

        Повертає:
        compressed_data (list): Список стиснутих токенів, кожен з яких
        представляється кортежем (довжина, зміщення).
        """
        compressed_data = []
        i = 0
        while i < len(data):
            match_length, match_offset = self.find_longest_match(data, i)
            if match_length > 2:
                compressed_data.append((match_length, match_offset))
                i += match_length
            else:
                compressed_data.append((0, data[i]))
                i += 1
        return compressed_data

    def find_longest_match(self, data, current_index):
        """
        Знаходить найдовшу відповідну підстроку в заданому вікні і буфері вигляду.

        Параметри:
        - data (str): Рядок, у якому шукається відповідна підстрока.
        - current_index (int): Поточний індекс, з якого починається пошук підстроки.

        Повертає:
        (best_length, best_offset) (tuple): Кортеж, що містить найдовшу довжину і
        зміщення знайденої підстроки.
        """
        end_index = min(current_index + self.lookahead_buffer_size, len(data))
        best_length = 0
        best_offset = 0

        for offset in range(1, self.window_size + 1):
            start_index = max(0, current_index - self.window_size)
            substring = data[current_index:current_index + offset]

            for j in range(start_index, current_index):
                match_length = 0
                while (
                    current_index + match_length < end_index and
                    data[j + match_length] == data[current_index + match_length]
                ):
                    match_length += 1

                if match_length > best_length:
                    best_length = match_length
                    best_offset = current_index - j

        return best_length, best_offset

    def decompress(self, compressed_data):
        """
        Розкодовує стиснуті дані, відновлюючи вихідний рядок.

        Параметри:
        - compressed_data (list): Список стиснутих токенів, кожен з яких
        представляється кортежем (довжина, зміщення).

        Повертає:
        decompressed_data (str): Розкодований рядок, відновлений зі стиснутих даних.
        """
        decompressed_data = []
        for token in compressed_data:
            length, offset = token
            if length > 0:
                start_index = len(decompressed_data) - offset
                for i in range(length):
                    decompressed_data.append(decompressed_data[start_index + i])
            else:
                decompressed_data.append(offset)
        return "".join(map(str, decompressed_data))
