board = [[0 for i in range(8)] for j in range(8)]
counter = 0
operation_counter = 0


def set_queen(i, j):
    global operation_counter
    operation_counter += 1
    for x in range(8):
        board[x][j] += 1
        board[i][x] += 1
        if 0 <= i + j - x < 8:
            board[i + j - x][x] += 1
        if 0 <= i - j + x < 8:
            board[i - j + x][x] += 1
    board[i][j] = -1


def remove_queen(i, j):
    for x in range(8):
        board[x][j] -= 1
        board[i][x] -= 1
        if 0 <= i + j - x < 8:
            board[i + j - x][x] -= 1
        if 0 <= i - j + x < 8:
            board[i - j + x][x] -= 1
    board[i][j] = 0


def print_position():
    global counter
    counter += 1
    alphabet = 'abcdefgh'
    answer = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == -1:
                answer.append(alphabet[j] + str(i + 1))
    print(','.join(answer))


def solve(i):
    for j in range(8):
        if board[i][j] == 0:
            set_queen(i, j)
            if i == 7:
                print_position()
            else:
                solve(i + 1)
            remove_queen(i, j)


def main():
    solve(0)                   # Вывод всех вариантов решения задачи
    print("Число решений: " + counter)             # Вывод числа решений
    print("Число проведенных операций (итераций): " + operation_counter)   # Вывод числа проведенных операций


if __name__ == "__main__":
    main()