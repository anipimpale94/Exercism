import numpy as np
def saddle_points(matrix):
    np_matrix = np.array(matrix)
    if len(np_matrix.shape) == 1:
        if matrix == []:
            return set()
        raise ValueError("Irregular Matrix")
    saddle_points = []
    for row_index in range(0, np_matrix.shape[0]):
        min_row = np_matrix[row_index][0]
        stack = [0]
        for column_index in range(1, np_matrix.shape[1]):
            if min_row < np_matrix[row_index][column_index]:
                stack = [column_index]
                min_row = np_matrix[row_index][column_index]
            elif min_row == np_matrix[row_index][column_index]:
                stack.append(column_index)

        for item in stack:
            flag = 1
            for row_index_saddle in range(0, np_matrix.shape[0]):
                if np_matrix[row_index][item] > np_matrix[row_index_saddle][item]:
                    flag = 0
                    break;
            if flag:
                saddle_points.append((row_index, item))               
    return set(saddle_points)
