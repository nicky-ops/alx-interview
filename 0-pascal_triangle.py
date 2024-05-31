#!/usr/bin/python3
'''
Representing the Pascal's triangle of n
'''
def pascal_triangle(n):
    '''
    This function creates the Pascal's triangle of n
    '''
    outer_list = []
    if n <= 0:
        return outer_list.append(inner_list)

    for i in range(1, n + 1):
        for j in range(0, n - i + 1):
   
        
