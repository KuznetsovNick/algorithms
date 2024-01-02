from modules.hash_table import HashTable
from modules.commands import Commands
import time
import matplotlib.pyplot as plt
import random


class TestHashTable:
    def __init__(self, kol, cmd):
        self.__kol = kol
        self.__cmd = cmd

    def start(self):
        plt.xlabel('Количество элементов')
        plt.ylabel('Время')
        plt.grid()
        y = []
        x = []
        if self.__cmd == Commands.INS:
            plt.title("Вставка")
            arr = list(range(self.__kol))
            random.shuffle(arr)
            h = HashTable()
            for i in range(self.__kol):
                t = time.perf_counter()
                h.insert(i, i)
                y.append(time.perf_counter() - t)
                x.append(i)
            plt.scatter(x, y, s=5)
            plt.show()
            return

        arr = list(range(self.__kol))
        random.shuffle(arr)
        h = HashTable()
        for i in range(self.__kol):
            h.insert(arr[i], i)

        if self.__cmd == Commands.FIND:
            plt.title("Поиск")
            for i in range(self.__kol):
                t = time.perf_counter()
                h.find(i)
                y.append(time.perf_counter() - t)
                x.append(i)
            plt.scatter(x, y, s=5)
            plt.show()
            return

        if self.__cmd == Commands.DEL:
            plt.title("Удаление")
            for i in range(self.__kol):
                t = time.perf_counter()
                h.delete(i)
                y.append(time.perf_counter() - t)
                x.append(i)
            plt.scatter(x, y, s=5)
            plt.show()
            return
