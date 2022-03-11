import copy
from random import randint
import time


def list_create():
    length = int(input("Введите длину массива: "))
    list_of_items = [randint(-500,500) for j in range(length)]
    print(list_of_items)
    return list_of_items


def Print(mas, n):
    for i in range(int(n)):
        print(mas[i], end=' ')
    print()


def delete_element(list_of_items):
    print("Хотите удалить элемент? ")
    ans = input()
    if ans == "да" or ans == "Да":
        index = int(input("Введите индекс: "))
        del list_of_items[index]
        Print(list_of_items, n - 1)


def insert_element(list_of_items):
    print("Хотите внести элемент? ")
    ans = input()
    if ans == "да" or ans == "Да":
        el = int(input("Введите число: "))
        index = int(input("Введите индекс: "))
        list_of_items.insert(index, el)
        Print(list_of_items, n + 1)


def binary_search(list_of_numbers, value):
    first = 0
    last = len(list_of_numbers) - 1
    index = -1

    while first <= last and index == -1:
        mid = (first + last) // 2
        if list_of_numbers[mid] == value:
            index = mid
        else:
            if value < list_of_numbers[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                print(lkpval, "не найден.")
                return False
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                print(lkpval, "не найден.")
                return False
            return self.right.findval(lkpval)
        else:
            print(self.data, ' найден.')
            return True

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


def make_a_tree(arr):
    root = Node(arr[0])
    for i in arr[1::]:
        root.insert(i)
    return root


def fibonacci_search(list_of_items, value):
    fib_minus_2 = 0
    fib_minus_1 = 1
    fib = fib_minus_1 + fib_minus_2
    while fib < len(list_of_items):
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib
        fib = fib_minus_1 + fib_minus_2
    index = -1
    while fib > 1:
        i = min(index + fib_minus_2, (len(list_of_items) - 1))
        if list_of_items[i] < value:
            fib = fib_minus_1
            fib_minus_1 = fib_minus_2
            fib_minus_2 = fib - fib_minus_1
            index = i
        elif list_of_items[i] > value:
            fib = fib_minus_2
            fib_minus_1 = fib_minus_1 - fib_minus_2
            fib_minus_2 = fib - fib_minus_1
        else:
            return i
    if fib_minus_1 and index < len(list_of_items) - 1 and list_of_items[index + 1] == value:
        return index + 1
    return -1


def interpolation_search(list_of_items, value):
    low = 0
    high = len(list_of_items) - 1
    while low <= high and value >= list_of_items[low] and value <= list_of_items[high]:
        index = low + int(((float(high - low) / (list_of_items[high] - list_of_items[low])) * (value - list_of_items[low])))
        if list_of_items[index] == value:
            return index
        if list_of_items[index] < value:
            low = index + 1
        else:
            high = index - 1
    return -1


def main():
    print("Исходный список:")
    list_of_items = list_create()
    list_of_items_binary = copy.deepcopy(list_of_items)
    list_of_items_binary.sort()
    print(list_of_items_binary)
    print("Бинарный поиск: ")
    value = int(input("Введите элемент для поиска: "))
    start_time_bin = time.time()
    print(f"Искомый элемент имеет индекс {binary_search(list_of_items_binary, value)}")
    end_time_bin = time.time() - start_time_bin
    print(f"Время работы бинарного поиска: {end_time_bin}")
    insert_element(list_of_items_binary)
    delete_element(list_of_items_binary)

    list_of_items_fibonacci = copy.deepcopy(list_of_items)
    list_of_items_fibonacci.sort()
    print(list_of_items_fibonacci)
    print("Фибоначчиев поиск: ")
    value = int(input("Введите элемент для поиска: "))
    start_time_fib = time.time()
    print(f"Искомый элемент имеет индекс {fibonacci_search(list_of_items_fibonacci, value)}")
    end_time_fib = time.time() - start_time_fib
    print(f"Время работы поиска Фибоначчи: {end_time_fib}")
    insert_element(list_of_items_fibonacci)
    delete_element(list_of_items_fibonacci)

    list_of_items_interpolation = copy.deepcopy(list_of_items)
    list_of_items_interpolation.sort()
    print(list_of_items_interpolation)
    print("Интерполяционный поиск: ")
    value = int(input("Введите элемент для поиска: "))
    start_time_int = time.time()
    print(f"Искомый элемент имеет индекс {interpolation_search(list_of_items_interpolation, value)}")
    end_time_int = time.time() - start_time_int
    print(f"Время работы интерполяционного поиска: {end_time_int}")
    insert_element(list_of_items_interpolation)
    delete_element(list_of_items_interpolation)

    list_of_items_tree = copy.deepcopy(list_of_items)
    root = make_a_tree(list_of_items_tree)
    value = int(input("Введите элемент для поиска: "))
    start_time_tree = time.time()
    result = root.findval(value)
    end_time_tree = time.time() - start_time_tree
    print(f"Время работы поиска в бинарном дереве: {end_time_tree}")
    ans = input("Хотите внести элемент? ")
    if ans == "да" or ans == "Да":
        val = int(input("Введите элемент, который хотите внести: "))
        root.insert(val)
        root.PrintTree()
    ans = input("Хотите удалить элемент? ")
    if ans == "да" or ans == "Да":
        val = int(input("Введите элемент, который хотите удалить: "))
        list_of_items_tree.remove(val)
        root = make_a_tree(list_of_items_tree)
        root.PrintTree()
    print(end_time_tree)


if __name__ == "__main__":
    main()