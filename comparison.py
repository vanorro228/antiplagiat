from levenshtein_distance import lev
import sys


def lev_metric(str_1, str_2):
    return (len(str_1) - lev(str_1, str_2)) / len(str_1)


if __name__ == '__main__':
    read, write = sys.argv[1:]
    files_path = open(read).read().split()
    i = 0
    lev_size = ''
    for i in range(0, len(files_path), 2):
        string_1 = ''.join(open(files_path[i], encoding='UTF-8').read().split())
        string_2 = ''.join(open(files_path[i + 1], encoding='UTF-8').read().split())
        lev_size += str(lev_metric(string_1, string_2)) + '\n'

    file_write = open(write, 'w')
    file_write.write(lev_size)
    file_write.close()
