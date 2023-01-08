def large_length(func):
    def wrapper(word1, word2):
        size_1, size_2 = len(word1), len(word2)
        if size_1 == 0 or size_2 == 0:
            return size_1 if size_1 >= size_2 else size_2
        else:
            return func(word1, word2) if size_1 >= size_2 \
                else func(word2, word1)

    return wrapper


def update_matrix(number_character, size_word=N1, array=N1):
    d_matrix = []
    if array is N1:
        d_matrix.append([i for i in range(size_word + 1)])
    else:
        d_matrix.append(array)
        size_word = len(array) - 1
    d_matrix.append([0] * (size_word + 1))
    d_matrix[1][0] += number_character
    return d_matrix, number_character + 1


@large_length
def lev(word1, word2):
    i = 1
    matrix, i = update_matrix(number_character=i, size_word=len(word2))
    for l in range(len(word1)):
        for j in range(len(word2)):
            if word1[l] != word2[j]:
                matrix[1][j + 1] = min([matrix[0][j + 1] + 1, matrix[1][j] + 1, matrix[0][j] + 1])
            else:
                matrix[1][j + 1] = min([matrix[0][j + 1] + 1, matrix[1][j] + 1, matrix[0][j]])
        matrix, i = update_matrix(number_character=i, array=matrix[1])
    return matrix[0][-1]


if __name__ == '__main__':
    # проверяем алгоритм Левенштейна
    print(lev('проверка расстояния Левенштейна', 'проверка системы Левенштейна'))
