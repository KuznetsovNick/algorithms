from modules.pair import Pair
import tabulate


class HashTable:

    def __init__(self):
        self.__size = 8
        self.__fullness = 0
        self.__fullness_koef = 1.7
        self.__data = []
        for i in range(self.__size):
            self.__data.append(Pair())

    def get_data(self):
        return self.__data

    def __str__(self):
        ret_string = ''
        for i in self.__data:
            ret_string += str(i) + '\n'
        return ret_string

    def print(self):
        head = ['key', 'value']
        arr = []
        for i in range(self.__size):
            arr.append([str(self.__data[i].first), str(self.__data[i].second)])
        print(tabulate.tabulate(arr, headers=head, tablefmt="outline"))

    def get_size(self):
        return self.__size

    def __expand_table(self):
        for i in range(self.__size, self.__size*2):
            self.__data.append(Pair())
        self.__size *= 2

    def __hash_func_1(self, x):
        # return 0
        return x % self.__size

    def __hash_func_2(self, x):
        # return 1
        return x % (self.__size - 1) + 1

    def __double_hash(self, x, i):
        return (self.__hash_func_1(x) + i * self.__hash_func_2(x)) % self.__size

    def __find_place(self, key):
        find_ind = 0
        ind = self.__double_hash(key, find_ind)

        found = False
        while not found:
            if self.__data[ind].is_empty():
                found = True
            else:
                find_ind += 1
                ind = self.__double_hash(key, find_ind)
        return ind

    def insert(self, key, value):
        ind = self.__find_elem(key)
        if ind == -1:
            ind = self.__find_place(key)

        self.__data[ind].first = key
        self.__data[ind].second = value

        self.__fullness += 1
        if self.__size < self.__fullness * self.__fullness_koef:
            self.__expand_table()

    def __find_elem(self, key):
        find_ind = 0
        ind = self.__double_hash(key, find_ind)

        found = False
        while not found:
            if not self.__data[ind].used and self.__data[ind].is_empty():
                ind = -1
                found = True
            elif self.__data[ind].first == key:
                found = True
            else:
                find_ind += 1
                ind = self.__double_hash(key, find_ind)
        return ind

    def find(self, key):
        ind = self.__find_elem(key)
        if ind == -1:
            return 'Not Found'
        return self.__data[ind].second

    def delete(self, key):
        ind = self.__find_elem(key)
        if ind == -1:
            print('Cannot be deleted')
        else:
            self.__data[ind].first = None
            self.__data[ind].second = None
            self.__data[ind].used = True
