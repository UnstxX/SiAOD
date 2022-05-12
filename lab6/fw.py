import math


# принимать должен матрицу смежности и начальныую с конечной вершины
# возвращать должен минимальный путь от одной вершины до другой
def fw(matrix, start, end):

    V = [[int(matrix[i][j]) if matrix[i][j] != 'math.inf' else math.inf
          for j in range(len(matrix))] for i in range(len(matrix))]

    def get_path(P, start, end):
        path = [start]
        while start != end:
            start = P[start][end]
            path = [start] + path

        return path

    N = len(V) # число вершин в графе
    P = [[v for v in range(N)] for u in range(N)] # начальный список предыдущих вершин для поиска кратчайших маршрутов

    for k in range(N):
        for i in range(N):
            for j in range(N):
                d = V[i][k] + V[k][j]
                if V[i][j] > d:
                    V[i][j] = d
                    P[i][j] = k     # номер промежуточной вершины при движении от i к j

    # нумерацця вершин начинается с нуля
    # start = 0
    # end = 7
    return get_path(P, end, start)
