from algorithms import work_with_algo

def work_with_txt(path, algorithm):
    string = ''
    with open(path, encoding="UTF-8") as file:
        data = file.read()
        data = '/'.join(data.split('\n'))

    decompressed, statistics = work_with_algo(algorithm, data)

    with open(path, 'w', encoding='UTF-8') as file:
        decompressed = decompressed.split('/')
        for element in decompressed:
            string += element + '\n'
        file.write(string)
    return statistics
