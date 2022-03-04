import copy
from random import randint
import time


def list_create():
    length = int(input("Введите длину массива: "))
    list_of_items = [randint(-500,500) for j in range(length)]
    list_of_items.sort()
    print(list_of_items)
    return list_of_items


def delete_element(list_of_items):
    index = int(input("Введите индекс числа, которое хотите удалить: "))
    del list_of_items[index]
    print(list_of_items)
    return list_of_items


def insert_element(list_of_items):
    index = int(input("Введите индекс числа, на который хотите вставить число: "))
    number = int(input("Введите число, которое хотите вставить: "))
    list_of_items.insert(index, number)
    print(list_of_items)
    return list_of_items


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
    print("Бинарный поиск: ")
    value = int(input("Введите элемент для поиска: "))
    print("Искомый элемент имеет индекс " + binary_search(list_of_items_binary, value))
    insert_element(list_of_items_binary)
    delete_element(list_of_items_binary)

    list_of_items_fibonacci = copy.deepcopy(list_of_items)
    print("Фибоначчиев поиск: ")
    value = int(input("Введите элемент для поиска: "))
    print("Искомый элемент имеет индекс " + fibonacci_search(list_of_items_fibonacci, value))
    insert_element(list_of_items_fibonacci)
    delete_element(list_of_items_fibonacci)

    list_of_items_interpolation = copy.deepcopy(list_of_items)
    print("Интерполяционный поиск: ")
    value = int(input("Введите элемент для поиска: "))
    print("Искомый элемент имеет индекс " + interpolation_search(list_of_items_interpolation, value))
    insert_element(list_of_items_interpolation)
    delete_element(list_of_items_interpolation)


if __name__ == "__main__":
    main()