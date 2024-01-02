from modules.avl_tree import AVLTree
from modules.commands import Commands
import time
import matplotlib.pyplot as plt
import random


class TestAVL:
    def __init__(self, kol, cmd):
        self.__kol = kol
        self.__cmd = cmd

    def start(self):
        arr = list(range(self.__kol))
        random.shuffle(arr)
        plt.xlabel('Количество элементов')
        plt.ylabel('Время')
        plt.grid()
        y = []
        x = []
        if self.__cmd == Commands.INS:
            plt.title("Вставка")
            avl = AVLTree()
            for i in range(self.__kol):
                t = time.perf_counter()
                avl.insert(arr[i], i)
                y.append(time.perf_counter() - t)
                x.append(i)
            plt.scatter(x, y, s=5)
            plt.show()
            return

        avl = AVLTree()
        for i in range(self.__kol):
            avl.insert(arr[i], i)

        if self.__cmd == Commands.FIND:
            plt.title("Поиск")
            for i in range(self.__kol):
                t = time.perf_counter()
                avl.find(i)
                y.append(time.perf_counter() - t)
                x.append(i)
            plt.scatter(x, y, s=5)
            plt.show()
            return

        if self.__cmd == Commands.DEL:
            plt.title("Удаление")
            for i in range(self.__kol):
                t = time.perf_counter()
                avl.remove(i)
                y.append(time.perf_counter() - t)
                x.append(i)
            plt.scatter(x, y, s=5)
            plt.show()
            return
