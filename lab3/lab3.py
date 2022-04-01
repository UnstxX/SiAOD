from datetime import datetime as t
import collections
from queue import PriorityQueue


# Алгоритм Кнута-Морриса-Пратта
def kmp(line, subline):
    p = [0] * len(subline)
    j = 0
    i = 1

    while i < len(subline):
        if subline[j] == subline[i]:
            p[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0;
                i += 1
            else:
                j = p[j - 1]
    print(p)

    m = len(subline)
    n = len(line)
    i = 0
    j = 0
    while i < n:
        if line[i] == subline[j]:
            i += 1
            j += 1
            if j == m:
                print(f"образ найден по индексу {i - (len(subline))}")
                break
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1

    if i == n and j != m:
        print("образ не найден")


line = str(input("Введите строку: "))
subline2 = str(input("Введите подстроку: "))
ans = str(input("Чувствительность к регистру Да/Нет: ").lower())
if ans == "нет":
    start_time = t.now()
    kmp(line.lower(), subline2.lower())
    print(t.now() - start_time)
elif ans == "да":
    start_time = t.now()
    kmp(line, subline2)
    print(t.now() - start_time)
else:
    print("Введите корректный ответ")


# Упрощенный алгоритм Бойера-Мура
def BM(line, subline):
    # Этап 1: формирование таблицы смещений
    S = set()  # уникальные символы в образе
    M = len(subline)  # число символов в образе
    d = {}  # словарь смещений

    for i in range(M - 2, -1, -1):  # итерации с предпоследнего символа
        if subline[i] not in S:  # если символ еще не добавлен в таблицу
            d[subline[i]] = M - i - 1
            S.add(subline[i])

    if subline[M - 1] not in S:  # отдельно формируем последний символ
        d[subline[M - 1]] = M

    d['*'] = M  # смещения для прочих символов
    print(d)

    # Этап 2: поиск образа в строке
    N = len(line)

    if N >= M:
        i = M - 1  # счетчик проверяемого символа в строке
        while (i < N):
            k = 0
            j = 0
            flBreak = False
            for j in range(M - 1, -1, -1):
                if line[i - k] != subline[j]:
                    if j == M - 1:
                        off = d[line[i]] if d.get(line[i], False) else d[
                            '*']  # смещение, если не равен последний символ образа
                    else:
                        off = d[subline[j]]  # смещение, если не равен не последний символ образа

                    i += off  # смещение счетчика строки
                    flBreak = True  # если несовпадение символа, то flBreak = True
                    break
                k += 1  # смещение для сравниваемого символа в строке
            if not flBreak:  # если дошли до начала образа, значит, все его символы совпали
                print(f"образ найден по индексу: {i - (M - 1)}")
                break
        else:
            print("образ не найден")
    else:
        print("образ не найден")


line2 = str(input("Введите строку: "))
subline2 = str(input("Введите подстроку: "))
ans = str(input("Чувствительность к регистру Да/Нет: ").lower())
if ans == "нет":
    start_time = t.now()
    BM(line2.lower(), subline2.lower())
    print(t.now() - start_time)
elif ans == "да":
    start_time = t.now()
    BM(line2, subline2)
    print(t.now() - start_time)
else:
    print("Введите корректный ответ")


test = collections.deque()
class Position:
    def __init__(self, position, start_distance,finish_distance):
        self.position = position
        self.start_distance = start_distance
        self.finish_distance = finish_distance

    def __str__(self):
        return '\n'.join((N*'{:3}').format(*[i%(N*N) for i in self.position[i:]]) for i in range(0, N*N, N))

    # Переопределяем метод less then для работы PriorityQueue
    def __lt__(self, other):
        return self.start_distance+self.finish_distance < other.start_distance+other.finish_distance
N = 4
# Генератор сдвигов
def shifts(position):
# Находим индекс нуля
    zeroPosition = position.index(0)
# Находим его позицию в поле 4х4, где i это номер строки, а j номер столбца
    i, j = divmod(zeroPosition, N)
    displacement = []
# В зависимости от местоположения нуля, смотрим варианты, куда его можно сдвинуть
    if i > 0: displacement.append(-N)     # вверх
    if i < N - 1: displacement.append(N)  # вниз
    if j > 0: displacement.append(-1)     # влево
    if j < N - 1: displacement.append(1)  # вправо
    for offset in displacement:
# считаем индексы новых позиций нуля
        swap = zeroPosition + offset
# Выводим новое состояние поля, где 0 сдвинут в одном из возможных направлений
        yield tuple(position[swap]
        if x==zeroPosition
        else position[zeroPosition]
        if x==swap
        else position[x]
        for x in range(N*N))


# Проверяет четность неправильных пар
def parityOfPairs(state):
    countOfPairs = 0
    for i in range(len(state)-1):
        if state[i] > state[i+1]:
            countOfPairs +=1
    return countOfPairs % 2
def fifteenGame(startState):
    terminalState = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
    # Если количество неправильных пар четное, то такая позиция нерешаема
    if parityOfPairs(startState)==0:
        print("Нет решений")
    else:
    # В противном случае создаем из начальной позиции кортеж
        startState= tuple(startState)
    # создаем экзмепляр класса, с кортежем стартовой позиции в качестве параметра,длинной пути от начала до текущей точки
    # и длиной от текущей позиции до конца
        p = Position(startState, 0,0)

    # Создаем экземпляр класса приоритетной очереди
        fieldStates= PriorityQueue()
    # Заносим в нее пару-это кортеж стартовой позиции, и вес данной вершины
        fieldStates.put(p)
    # Создаем множество посещенных вершин
        closePoints = set([p])
    # Создаем словарь в котором будем хранить позиции, где для каждой будет определена ее предыдущая позиция
        parents = {p.position: None}

    # Пока позиция не будет равна решению
        while p.position != terminalState:
    # Получаем приоритетную позицию
            p =fieldStates.get()


    # для каждого варианта передвижения нуля в одном состоянии поля
            for k in shifts(p.position):
                count= 0
    # Если такой вариант передвижения не находится в списке посещенных
                if k not in closePoints:
    # Расчитаем растояние до терминального состояния, это количество цифр стоящих не на своих местах
                    for m in range(len(k)):
                        if k[m] != terminalState[m]:
                            count+=1

    # То мы заносим его в очередь, с состоянием в качестве параметра, длиной пути от старта до текущего состояния
    # и длиной до финиша

                    fieldStates.put(Position(k, p.start_distance +1,p.finish_distance+count))
    # в словарь добавляем новый ключ, то есть эту позицию, его значением будет предыдущая позиция
                    parents[k] = p

    # Добавляем этот вариант перемещения в посещенный
                    closePoints.add(k)

        path = []
        x = p
        previous = p
        while p.position != startState:

    # Берем из словаря родителя текущего состояния поля

            p = parents[p.position]


    # Запоминаем индекс нуля и


# Запоминаем индекс нуля из текущего состояния и по этому индексу находим элемент, который сдвинули в предыдущем состоянии
            number = p.position[previous.position.index(0)]
            path.append(number)
    # Предыдущее состояние делаем текущим
            previous = p
            test.append(p)

    # Разворачиваем путь, чтобы получить путь от первого до последнего сдвига
        path.reverse()
    if parityOfPairs(startState)!=0:
        for reverse_print in range(len(path)):
            print(f"\n{test.pop()}")
        print(f"\n{x}\n\n{path}\nЧисло шагов: {len(path)}")
startState = [1,2,3,4,5,6,7,8,9,10,11,12,0,13,14,15]
fifteenGame(startState)