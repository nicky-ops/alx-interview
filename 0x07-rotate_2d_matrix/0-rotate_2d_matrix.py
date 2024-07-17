#!/usr/bin/python3
'''
Rotate 2D Matrix
'''


def rotate_2d_matrix(matrix):
    '''
    This function taxes an n X n matrix and rotates it by 90 degrees clockwise
    '''
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
