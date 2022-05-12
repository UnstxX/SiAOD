def convert_adjacency_matrix(matrix):
    result_list = [(i, j, int(matrix[i][j]))
                   for j in range(len(matrix))
                   for i in range(len(matrix))
                   if matrix[i][j] != 'math.inf']

    return result_list
