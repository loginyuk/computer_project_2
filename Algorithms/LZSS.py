from struct import Struct
import time
class LZSS:
    """
    Клас, що реалізує алгоритм LZSS для стиснення та розпакування даних.
    """

    def __init__(self):
        pass

    def decode(self, compressed_data):
        """
        Розпаковує стислі дані, використовуючи алгоритм LZSS.

        :param compressed_data: Стислі дані, що підлягають розпакуванню.
        :return: Розпаковані дані.
        """
        if not compressed_data[0]:
            return compressed_data

        uncompressed_size = (compressed_data[2] << 8) | compressed_data[1]
        data_iterator = iter(compressed_data[3:])
        control = 1
        uncompressed_data = bytearray()

        while len(uncompressed_data) < uncompressed_size:
            if control == 1:
                control = 0x10000 | next(data_iterator) | (next(data_iterator) << 8)

            if control & 1:
                pointer = next(data_iterator) | (next(data_iterator) << 8)
                length = (pointer >> 11) + 3
                pointer &= 0x7FF
                pointer += 1
                for i in range(length):
                    uncompressed_data.append(uncompressed_data[-pointer])
            else:
                uncompressed_data.append(next(data_iterator))

            control >>= 1

        return bytes(uncompressed_data)

    def _search(self, data, position, size):
        """
        Внутрішня функція пошуку найкращого збігу підстроки у вхідних даних.

        :param data: Вхідні дані.
        :param position: Початкова позиція для пошуку.
        :param size: Розмір вхідних даних.
        :return: Позицію та довжину найкращого збігу підстроки.
        """
        max_length = min(0x22, size - position)
        if max_length < 3:
            return 0, 0

        max_position = max(0, position - 0x800)
        hit_position, hit_length = 0, 3

        if max_position < position:
            substring_length = data[max_position : position + hit_length].find(data[position : position + hit_length])
            while substring_length < (position - max_position):
                while (hit_length < max_length) and (data[position + hit_length] == data[max_position + substring_length + hit_length]):
                    hit_length += 1

                max_position += substring_length
                hit_position = max_position

                if hit_length == max_length:
                    return hit_position, hit_length

                max_position += 1
                hit_length += 1

                if max_position >= position:
                    break

                substring_length = data[max_position : position + hit_length].find(data[position : position + hit_length])

        if hit_length < 4:
            hit_length = 1

        return hit_position, hit_length - 1

    def encode(self, data):
        """
        Стискає дані за допомогою алгоритму LZSS.

        :param data: Вхідні дані, що підлягають стисканню.
        :return: Стислі дані.
        """
        HW = Struct("<H")

        max_length = 0x22
        uncompressed_size = len(data)
        compressed_data = bytearray(b'\x01')
        compressed_data.extend(HW.pack(uncompressed_size))

        control, commands = 0, 3
        position, flag = 0, 1

        compressed_data.append(0)
        compressed_data.append(0)

        while position < uncompressed_size:
            hit_position, hit_length = self._search(data, position, uncompressed_size)

            if hit_length < 3:
                compressed_data.append(data[position])
                position += 1
            else:
                next_hit_position, next_hit_length = self._search(data, position + 1, uncompressed_size)

                if (hit_length + 1) < next_hit_length:
                    compressed_data.append(data[position])
                    position += 1
                    flag <<= 1

                    if flag & 0x10000:
                        HW.pack_into(compressed_data, commands, control)
                        control, flag = 0, 1
                        commands = len(compressed_data)
                        compressed_data.append(0)
                        compressed_data.append(0)

                    hit_length = next_hit_length
                    hit_position = next_hit_position

                control |= flag

                encoded_value = position - hit_position - 1
                position += hit_length
                hit_length -= 3
                encoded_value |= hit_length << 11

                compressed_data.extend(HW.pack(encoded_value))

            flag <<= 1

            if flag & 0x10000:
                HW.pack_into(compressed_data, commands, control)
                control, flag = 0, 1
                commands = len(compressed_data)
                compressed_data.append(0)
                compressed_data.append(0)

        if flag == 1:
            del compressed_data[-2:]
        else:
            HW.pack_into(compressed_data, commands, control)

        return bytes(compressed_data)
